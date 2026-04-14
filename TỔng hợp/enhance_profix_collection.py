import json
import os

def enhance_collection(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. Update Auth at Collection Level
    data["auth"] = {
        "type": "bearer",
        "bearer": [{"key": "token", "value": "{{bearerToken}}", "type": "string"}]
    }

    # Standard test scripts to inject
    standard_tests = [
        "pm.test('Status code is 200', function () { pm.response.to.have.status(200); });",
        "pm.test('Response time is less than 1000ms', function () { pm.expect(pm.response.responseTime).to.be.below(1000); });",
        "pm.test('Response is valid JSON', function () { pm.response.to.be.json; });"
    ]

    def process_items(items):
        for item in items:
            if "item" in item:  # It is a folder
                process_items(item["item"])
            elif "request" in item:  # It is a request
                # Ensure "event" list exists
                if "event" not in item:
                    item["event"] = []
                
                # Check for "test" event
                test_event = next((e for e in item["event"] if e["listen"] == "test"), None)
                if not test_event:
                    test_event = {"listen": "test", "script": {"type": "text/javascript", "exec": []}}
                    item["event"].append(test_event)
                
                # Special logic for Login
                if "login" in item["name"].lower() or "đăng nhập" in item["name"].lower():
                    login_script = [
                        "var jsonData = pm.response.json();",
                        "var token = jsonData.token || (jsonData.data && (jsonData.data.token || jsonData.data.accessToken));",
                        "if (token) {",
                        "    pm.environment.set('bearerToken', token);",
                        "    pm.collectionVariables.set('bearerToken', token);",
                        "    console.log('Smart Auth: Token captured successfully');",
                        "}",
                        "pm.test('Login Successful', function() { pm.response.to.have.status(200); });"
                    ]
                    test_event["script"]["exec"] = login_script
                else:
                    # Inject standard tests if not already there
                    current_script = test_event["script"]["exec"]
                    # Clean up and add standard ones
                    test_event["script"]["exec"] = standard_tests
                
                # Dynamic Chaining: capture IDs from /list requests
                if "/list" in item["request"]["url"].get("raw", ""):
                    chain_script = [
                        "var jsonData = pm.response.json();",
                        "var listData = jsonData.data || jsonData.content || (jsonData.data && jsonData.data.content);",
                        "if (listData && listData.length > 0) {",
                        "    var id = listData[0].id || listData[0].userId || listData[0].productId;",
                        "    if(id) { pm.collectionVariables.set('lastCapturedId', id); }",
                        "}"
                    ]
                    test_event["script"]["exec"].extend(chain_script)

    process_items(data["item"])

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    src = "/Users/mac/antigravity-testing-kit/API testing/Profix API Copy 2.postman_collection.json"
    dest = "/Users/mac/antigravity-testing-kit/API testing/Profix_API_Smart_Enhanced.json"
    enhance_collection(src, dest)
    print(f"Enhancement complete: {dest}")
