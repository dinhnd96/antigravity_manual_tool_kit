import json
import os

collection_path = "/Users/mac/antigravity-testing-kit/Profix API.postman_collection.json"
output_path = "/Users/mac/antigravity-testing-kit/Profix_API_Automation.postman_collection.json"

def add_tests_to_item(item):
    if "item" in item:
        for sub_item in item["item"]:
            add_tests_to_item(sub_item)
    
    if "request" in item:
        name = item.get("name", "").lower()
        method = item["request"].get("method", "GET")
        
        # Initialize event if not exists
        if "event" not in item:
            item["event"] = []
        
        test_scripts = []
        
        # 1. Base Status Code Test
        if method == "POST" and ("create" in name or "đăng ký" in name):
            test_scripts.append('pm.test("Status code is 200 or 201", function () { pm.expect(pm.response.code).to.be.oneOf([200, 201]); });')
        else:
            test_scripts.append('pm.test("Status code is 200", function () { pm.response.to.have.status(200); });')
        
        # 2. Performance Test
        test_scripts.append('pm.test("Response time is less than 1000ms", function () { pm.expect(pm.response.responseTime).to.be.below(1000); });')
        
        # 3. Specific Logic: Login
        if "login" in name or "đăng nhập" in name:
            test_scripts.append('if (pm.response.code === 200) { var jsonData = pm.response.json(); if(jsonData.token) { pm.environment.set("bearerToken", jsonData.token); console.log("Token saved: " + jsonData.token); } }')
        
        # 4. JSON Structure Test
        test_scripts.append('pm.test("Response is valid JSON", function () { pm.response.to.be.withBody; pm.response.to.be.json; });')
        
        # Update or Add the test event
        test_event = {
            "listen": "test",
            "script": {
                "exec": test_scripts,
                "type": "text/javascript"
            }
        }
        
        # Avoid duplicate test listeners
        item["event"] = [ev for ev in item["event"] if ev.get("listen") != "test"]
        item["event"].append(test_event)

with open(collection_path, 'r') as f:
    data = json.load(f)

for item in data["item"]:
    add_tests_to_item(item)

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Generated Automation Collection at: {output_path}")
