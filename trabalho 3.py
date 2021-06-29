N = int(input('Quantos alunos? '))

students = {}

for i in range(1, N+1):
  name = input(f'Nome do aluno {i}: ')
  grades = []

  for j in range(1, 5):
    grade = float(input(f'Nota {j} do aluno {i}: '))
    grades.append(grade)

  students[name] = grades

for name, grades in students.items():
  average = sum(grades) / len(grades)
  result = 'aprovado' if average >= 7.0 else 'reprovado'
  print(f'O aluno {name} foi {result} com média {average:.1f}')