def study_schedule(permanence_periods, target_time):
    # Verificação se target_time é nulo
    if target_time is None:
        return None

    # Verificação de formato e validade dos períodos de permanência
    if not all(
        isinstance(period, tuple)
        and len(period) == 2
        and isinstance(period[0], int)
        and isinstance(period[1], int)
        for period in permanence_periods
    ):
        return None

    # Inicializa o contador de estudantes
    students_count = 0

    # Itera sobre os períodos de permanência
    for start, end in permanence_periods:
        # Verifica se o target_time está dentro do período atual
        if start <= target_time <= end:
            students_count += 1

    return students_count


# Exemplo de uso
presence_periods = [(1, 5), (2, 6), (4, 8), (7, 10)]
target_time = 10
result = study_schedule(presence_periods, target_time)
print(result)
