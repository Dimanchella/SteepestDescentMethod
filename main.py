import json
import sys

from steepest_descent import SteepestDecent

ERROR_CODE = -1

if __name__ == '__main__':
    functions: dict
    try:
        with open("input.json", "r") as json_file:
            functions = json.load(json_file)
        # error_check(sources, purposes, table)
    except FileNotFoundError as fnfe:
        print(f"Файл input.json не найден.\n{fnfe}")
        sys.exit(ERROR_CODE)

    for func_name in functions:
        steedes = SteepestDecent(
            functions[func_name]['func'],
            functions[func_name]['start_x']
        )
        steedes.calculate_minimize()
        print(
            f"{func_name}: {functions[func_name]['str_f']}\n"
            f"start point: {functions[func_name]['start_x']}"
        )
        xsh = steedes.get_xs_history()
        vsh = steedes.get_values_history()
        gsh = steedes.get_grad_history()
        alsh = steedes.get_alpha_history()
        apsh = steedes.get_approx_history()

        strings = [f" 1 point = {xsh[0]} fx = {vsh[0]}"]
        for i in range(len(gsh)):
            strings.append(
                f" {i + 2} point = {xsh[i + 1]} fx = {vsh[i + 1]}"
                f"\n {' ' * len(str(i + 2))} grad = {gsh[i]} alpha = {alsh[i]} approx = {apsh[i]}"
            )
        print(
            '\n'.join(strings)
            + f"\n\nRESULT = {vsh[-1]}")