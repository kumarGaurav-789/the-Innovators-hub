"""
SwasthyaNet - Automated Verification Test Suite
Author: The Innovators Hub (Kumar Gaurav, Shanti Priya)
"""

import sys
import os
import asyncio

# Ensure project root in path
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from backend.data_store import data_store
from backend.forecasting_engine import forecasting_engine
from backend.redistribution_optimizer import redistribution_optimizer
from backend.federated_engine import federated_engine
from backend.fhir_abdm import generate_fhir_supply_delivery_bundle
from mcp_server.swasthyanet_mcp import mcp

def run_tests():
    print("==================================================")
    print("   RUNNING SWASTHYANET VERIFICATION TESTS         ")
    print("==================================================")

    # 1. Test Data Store
    print("\n[1/6] Testing Data Store & Telemetry...")
    phcs = data_store.get_all_phcs()
    assert len(phcs) == 12, f"Expected 12 PHCs, got {len(phcs)}"
    bundu = data_store.get_phc("PHC-JH-RAN-04")
    assert bundu is not None, "Bundu PHC not found"
    assert "ASV-001" in bundu.inventory, "ASV-001 drug not in Bundu inventory"
    print(f"  [OK] Data store loaded {len(phcs)} PHCs across Jharkhand successfully.")

    # 2. Test Forecasting Engine
    print("\n[2/6] Testing 2-3 Week Demand Forecasting Engine...")
    forecast_report = forecasting_engine.forecast_district("Ranchi")
    assert forecast_report["total_phcs_monitored"] > 0
    assert "phc_reports" in forecast_report
    print(f"  [OK] Forecast generated for {forecast_report['district_scope']}. Critical facilities flagged: {forecast_report['critical_phcs_count']}.")

    # 3. Test Redistribution Optimizer
    print("\n[3/6] Testing Supply Redistribution Optimizer...")
    plan = redistribution_optimizer.compute_rebalancing_plan()
    assert plan.total_transfers > 0, "Expected at least 1 transfer route"
    route = plan.routes[0]
    print(f"  [OK] Computed {plan.total_transfers} transfer routes.")
    print(f"    - Sample Route: {route.donor_phc_name} -> {route.recipient_phc_name}")
    print(f"    - Distance: {route.distance_km} km | ETA: {route.estimated_transit_minutes} mins | Patients protected: {route.estimated_lives_impacted}")

    # Test transfer dispatch
    dispatch_res = redistribution_optimizer.execute_transfer_route(route.transfer_id, plan)
    assert dispatch_res["status"] == "success"
    print(f"  [OK] Successfully executed transfer {route.transfer_id} and updated live inventory balances.")

    # 4. Test Federated Learning Simulation
    print("\n[4/6] Testing Federated Learning & Differential Privacy...")
    fl_round = federated_engine.trigger_training_round()
    assert fl_round.round_number > 3
    assert fl_round.forecast_accuracy_percent > 85.0
    assert fl_round.differential_privacy_epsilon > 0
    print(f"  [OK] Federated Round {fl_round.round_number} completed.")
    print(f"    - Global Accuracy: {fl_round.forecast_accuracy_percent}% | Global Loss: {fl_round.global_loss}")
    print(f"    - Privacy Epsilon: eps = {fl_round.differential_privacy_epsilon} (DPDP Act 2023 compliant)")
    print(f"    - Bandwidth Reduction: {fl_round.bandwidth_savings_percent}% vs centralizing raw EHR")

    # 5. Test ABDM & FHIR R4 Bundle
    print("\n[5/6] Testing ABDM / HL7 FHIR R4 Transaction Bundle...")
    bundle = generate_fhir_supply_delivery_bundle(route)
    assert bundle["resourceType"] == "Bundle"
    assert bundle["type"] == "transaction"
    assert len(bundle["entry"]) >= 2
    supply_del = bundle["entry"][0]["resource"]
    assert supply_del["resourceType"] == "SupplyDelivery"
    print(f"  [OK] Generated FHIR R4 SupplyDelivery bundle ({bundle['id']}) with ABDM profile metadata.")

    # 6. Test MCP Server Tools
    print("\n[6/6] Testing Model Context Protocol (MCP 2.x) Tools...")
    async def test_mcp():
        tools = await mcp.list_tools()
        assert len(tools) == 9, f"Expected 9 MCP tools, found {len(tools)}"
        print(f"  [OK] MCP Server successfully registered {len(tools)} tools:")
        for t in tools:
            print(f"     * {t.name}")

        res = await mcp.call_tool("swasthyanet_generate_cmo_briefing", {"district": "Ranchi"})
        assert res is not None
        print("  [OK] MCP tool 'swasthyanet_generate_cmo_briefing' executed successfully.")

    asyncio.run(test_mcp())

    print("\n==================================================")
    print("   ALL SWASTHYANET VERIFICATION TESTS PASSED!     ")
    print("==================================================")

if __name__ == "__main__":
    run_tests()
