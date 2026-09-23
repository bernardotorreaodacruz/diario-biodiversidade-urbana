import csv
import os


ARQUIVO = "biodiversidade_urbana.csv"


def criar_arquivo():
    """Cria o arquivo CSV caso ele ainda não exista."""
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(
                ["Espécie/Animal", "Bairro", "Data", "Observação"]
            )


def adicionar_registro():
    print("\n--- Nova observação ---")

    especie = input("O que você viu? ").strip()

    if not especie:
        print("A espécie é obrigatória.")
        return

    bairro = input("Bairro: ").strip()
    data = input("Data: ").strip()
    observacao = input("Observação: ").strip()

    if not bairro:
        bairro = "Não informado"

    if not data:
        data = "Não informado"

    if not observacao:
        observacao = "Não informado"

    try:
        with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([especie, bairro, data, observacao])

        print("Registro salvo com sucesso!")

    except PermissionError:
        print("Não foi possível salvar o registro.")
        print("Verifique se o arquivo está aberto em outro programa.")


def ver_registros():
    print("\n--- Seu Diário de Biodiversidade ---")

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            registros = list(leitor)

        if len(registros) <= 1:
            print("Nenhuma observação cadastrada ainda.")
            return

        for numero, registro in enumerate(registros[1:], start=1):
            especie = registro[0]
            bairro = registro[1]
            data = registro[2]
            observacao = registro[3]

            print(
                f"\n{numero}. {especie}"
                f"\n   Local: {bairro}"
                f"\n   Data: {data}"
                f"\n   Observação: {observacao}"
            )

    except FileNotFoundError:
        print("O arquivo ainda não existe.")


def apagar_registro():
    print("\n--- Apagar registro ---")

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            registros = list(leitor)

        if len(registros) <= 1:
            print("Não há registros para apagar.")
            return

        for numero, registro in enumerate(registros[1:], start=1):
            print(f"{numero}. {registro[0]} - {registro[1]}")

        escolha = input(
            "\nDigite o número do registro que deseja apagar "
            "(0 para cancelar): "
        ).strip()

        if escolha == "0":
            print("Operação cancelada.")
            return

        try:
            escolha = int(escolha)
        except ValueError:
            print("Digite apenas um número.")
            return

        if escolha < 1 or escolha >= len(registros):
            print("Número de registro inválido.")
            return

        registro_removido = registros.pop(escolha)

        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(registros)

        print(
            f"Registro de '{registro_removido[0]}' "
            "apagado com sucesso!"
        )

    except FileNotFoundError:
        print("O arquivo ainda não existe.")


def menu():
    criar_arquivo()

    while True:
        print("\n=== Diário de Biodiversidade Urbana ===")
        print("1. Adicionar observação")
        print("2. Ver registros")
        print("3. Apagar registro")
        print("4. Sair")

        escolha = input("\nEscolha uma opção: ").strip()

        if escolha == "1":
            adicionar_registro()

        elif escolha == "2":
            ver_registros()

        elif escolha == "3":
            apagar_registro()

        elif escolha == "4":
            print("\nAté a próxima observação!")
            break

        else:
            print("Opção inválida. Escolha entre 1 e 4.")


if __name__ == "__main__":
    menu()