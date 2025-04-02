from pathlib import Path
import json
from typing import List, Dict

class Aluno:
    def __init__(self,nome: str, nota: float):
    #representa um aluno com nome e nota
    #ex:
    #nota(float): nota do aluno

        self.nome = nome.strip().title()
        self.nota = float(nota)
    
    def to_dict(self) -> Dict[str,float]:
    #retorna o aluno como um dicionario com nome e nota
        return {self.nome: self.nota}
    
    def __str__(self) -> str:
    #representa em string do aluno no formato csv
        return f"{self.nome},{self.nota:.1f}"
        
    
class Gerenciador_Alunos:

    def __init__(self, base_dir: Path):

        self.csv_path = base_dir / "alunos.csv"
        self.json_path = base_dir / "alunos.json"
        self.txt_path = base_dir / "Alunos.txt"
        self.alunos: Dict[str, float] = self._carregar()

    def _carregar(self) -> Dict[str, float]:
    #carrega os dados se existir o arquivo CSV
        if self.csv_path.exists():
            try:
                with open(self.csv_path,"r") as f:
                    return {
                        nome: float(nota)
                        for nome, nota in (linha.strip().split(",") for linha in f)
                    }
            except FileNotFoundError:
                print("arquivo CSV não encontrado.")
            except ValueError as ve:
                print("Erro ao converter nota para float: {ve}")
            except OSError as oe:
                print("Erro de sistemas ao acessar o arquivo: {oe}")
        return{}
    def salvar(self) -> None:
        #salvar os dados dos alunos nos formatos CSV,TXT,JSON
        try:
            with open(self.csv_path, "w") as f_csv,open(self.txt_path,"w") as f_txt, open(self.json_path,"w") as f_json:
                for nome, nota in self.alunos.items():
                    linha = f"{nome},{nota:.1f}\n"
                    f_csv.write(linha)
                    f_txt.write(f"{nome} tem nota {nota:.1f}\n")
                json.dump(self.alunos, f_json, indent=4)

        except Exception as e:
            print(f"Erro ao salvar os arquivos: {e}")
        
    def cadastrar(self, aluno:Aluno) -> bool:
        #cadastra ou atualisa um aluno no dicionario e salva os dados.

        self.alunos[aluno.nome] = aluno.nota
        self.salvar()
        return True
    
    def remover(self, nome: str) -> bool:
        if nome in self.alunos:
            del self.alunos[nome]
            self.salvar()
            return True
        return False
 
    def alterar_nota(self,nome: str, nova_nota: float) -> bool:

        if nome in self.alunos:
            self.alunos[nome] = nova_nota
            self.salvar()
            return True
        return False
    
    def listar(self) -> List[str]:
        return[f"{nome}, {nota:.1f}" for nome, nota in self.alunos.items()]
    
    def buscar(self, nome: str) -> str:

        if nome in self.alunos:
            return f"{nome},{self.alunos[nome]}"
        return "Aluno não encontrado"
    
if __name__ == "__main__":
    base_dir = Path(__file__).parent
    gerenciador = Gerenciador_Alunos(base_dir)

    print("cadastrando:", gerenciador.cadastrar(Aluno("Rafael",8.0)))
    print("lendo:", gerenciador.buscar("Rafael"))
    print("Lista completa", gerenciador.listar())
    print("Removendo:",gerenciador.remover("Rafael"))
    print("Lista pós remoção", gerenciador.listar())
    print("Novo cadastro:", gerenciador.cadastrar(Aluno("Rafael",7.4)))
    print("Alterando nota:", gerenciador.alterar_nota("Rafael",10.0))
    print("lista final", gerenciador.listar())


