def LeadsToSolution(solution, test_solution) -> bool:
    """Presudo code for backtracing.
    
    Args:
        solution: the result we want.
        test_solution: the solution we are trying.
    
    Returns:
        return solved or not.
    """
    if not solution(test_solution):
        return False
    if solution(test_solution):
        return True
    for other in solution(test_solution):
        if LeadsToSolution(solution, other):
            return True
    return False


