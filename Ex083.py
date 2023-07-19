#Exercício 083 - Ver se uma expressão é válida ou inválida.
teste = str(input("Digite uma expressão: "))
problem = []
pos = 0
for c in teste:
    if teste[pos] in "([{" and teste[pos+1] in (")]}"):
        problem.append(1)
        break
    if teste[pos] in "([{])}":
        problem.append(teste[pos])
    if "(" in problem and ")" in problem:
        problem.remove("(")
        problem.remove(")")
    if "[" in problem and "]" in problem:
        problem.remove("[")
        problem.remove("]")
    if "{" in problem and "}" in problem:
        problem.remove("{")
        problem.remove("}")
    pos+=1
if len(problem) > 0:
    print("A expressão é inválida!")
else:
    print("A expressão é válida!!! =D")

print(problem)
