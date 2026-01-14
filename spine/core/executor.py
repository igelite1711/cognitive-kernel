
def executor(state, tools):
    if state.status == "STOP": return state
    
    print(f"🚀 Executing {len(state.plan.get('steps', []))} steps...")
    
    for step in state.plan.get('steps', []):
        action = step['action']
        tool_input = step['input']
        
        if action in tools:
            # Execute the tool from registry
            result = tools[action](tool_input)
            state.step_results.append({
                "step_id": step['id'],
                "result": result
            })
        else:
            state.step_results.append({
                "step_id": step['id'],
                "result": f"Error: Tool {action} not found"
            })
            
    return state
