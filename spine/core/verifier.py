
def verifier(state, validators=None):
    if state.status == "STOP": return state
    
    # Simple verification: Did we get results?
    if not state.step_results:
        state.status = "FAIL"
        state.errors.append("No steps were executed.")
        return state
        
    # Aggregate results for final output
    final_output = ""
    for res in state.step_results:
        final_output += str(res['result']) + "\n"
    
    state.output = final_output.strip()
    state.status = "OK"
    return state
