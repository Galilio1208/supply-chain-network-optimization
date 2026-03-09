import pandas as pd
import pulp
import os

dist = pd.read_excel("data/distance_matrix_final.xlsx")

counties = dist["county"].unique().tolist()
warehouses = dist["warehouse"].unique().tolist()

distance = {(row["county"], row["warehouse"]): row["distance_km"]
            for _, row in dist.iterrows()}

population = dist.groupby("county")["population"].first().to_dict()

scenarios = [2,3,4]

results_summary = []

for p in scenarios:

    print(f"\nRunning scenario with {p} warehouses")

    model = pulp.LpProblem("Warehouse_Optimization", pulp.LpMinimize)

    open_wh = pulp.LpVariable.dicts("OpenWH", warehouses, 0, 1, pulp.LpBinary)
    assign = pulp.LpVariable.dicts("Assign", (counties, warehouses), 0, 1, pulp.LpBinary)

    model += pulp.lpSum(
        population[c] * distance[(c,w)] * assign[c][w]
        for c in counties for w in warehouses
    )

    for c in counties:
        model += pulp.lpSum(assign[c][w] for w in warehouses) == 1

    for c in counties:
        for w in warehouses:
            model += assign[c][w] <= open_wh[w]

    model += pulp.lpSum(open_wh[w] for w in warehouses) == p

    model.solve()

    selected = [w for w in warehouses if open_wh[w].value()==1]

    assignments = []

    for c in counties:
        for w in warehouses:
            if assign[c][w].value()==1:
                assignments.append({
                    "county":c,
                    "warehouse":w,
                    "population":population[c],
                    "distance_km":distance[(c,w)]
                })

    assignments_df = pd.DataFrame(assignments)

    total_distance = (assignments_df["population"] * assignments_df["distance_km"]).sum()

    avg_distance = total_distance / assignments_df["population"].sum()

    results_summary.append({
        "warehouses":p,
        "avg_distance_km":avg_distance,
        "selected_locations":", ".join(selected)
    })

    print("Selected Warehouses:", selected)
    print("Average Distance:", avg_distance)

summary_df = pd.DataFrame(results_summary)

os.makedirs("outputs", exist_ok=True)

summary_df.to_excel("outputs/scenario_comparison.xlsx", index=False)

print("\nScenario results saved to outputs/scenario_comparison.xlsx")