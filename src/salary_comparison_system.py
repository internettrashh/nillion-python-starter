from nada_dsl import *

def nada_main():
    # Initialize parties
    party1 = Party(name="Eva")
    party2 = Party(name="Liam")
    party3 = Party(name="Noah")
    party4 = Party(name="Diana")

    # Salaries for each party
    eva_salary = SecretInteger(Input(name="eva_salary", party=party1))
    liam_salary = SecretInteger(Input(name="liam_salary", party=party2))
    noah_salary = SecretInteger(Input(name="noah_salary", party=party3))
    diana_salary = SecretInteger(Input(name="diana_salary", party=party4))

    # Calculate total and average salary
    total_salary = eva_salary + liam_salary + noah_salary + diana_salary
    average_salary = total_salary / Integer(4)

    # Determine if each party's salary is above the average
    eva_above_avg = (eva_salary > average_salary).if_else(Integer(1), Integer(0))
    liam_above_avg = (liam_salary > average_salary).if_else(Integer(1), Integer(0))
    noah_above_avg = (noah_salary > average_salary).if_else(Integer(1), Integer(0))
    diana_above_avg = (diana_salary > average_salary).if_else(Integer(1), Integer(0))

    # Output whether each party's salary is above the average
    out_eva = Output(eva_above_avg, "eva_above_avg", party1)
    out_liam = Output(liam_above_avg, "liam_above_avg", party2)
    out_noah = Output(noah_above_avg, "noah_above_avg", party3)
    out_diana = Output(diana_above_avg, "diana_above_avg", party4)

    return [out_eva, out_liam, out_noah, out_diana]