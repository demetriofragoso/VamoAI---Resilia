def comparar_idade (idade_demetrio, idade_ada):
    comparar_idade = (idade_demetrio - idade_ada)
    print(f"A Ada e Demétrio tem uma diferença de idade de {comparar_idade} anos.")

def comparar_cidade (cidade_demetrio, cidade_ada):
    comparar_cidade = (cidade_demetrio, cidade_ada)
    print(f"A Ada e Demétrio moram em cidades diferentes, Demétrio mora em {cidade_demetrio} e Ada mora em {cidade_ada}")
def comparar_pais (pais_demetrio, pais_ada):
    comparar_pais = (pais_demetrio, pais_ada)
    print(f"A Ada e Demétrio moram em paises diferentes, Demétrio mora em {pais_demetrio} e Ada mora em {pais_ada}")

print("Abaixo irei comparar alguns dados meus com a Ada Lovelace (primeira programadora de toda a história).")
print('{::^100}'.format("Comparar dados"))
comparar_idade(33,36)
comparar_cidade("joão Pessoa-PB","Londres")
comparar_pais("Brasil", "Inglaterra")