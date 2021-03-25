#Nesta tentativa, eu tive o resultado que queria, mas nada automatizado por um programa.

#Aqui primeiramente eu baixaria o codigo json PELO FIREFOX, saindo um aquivo .php.json.
# que por algum motivo, esse arquivo consegue ser convertido por essa função abaixo, sendo orientado em records e lines.

df = pd.read_json('c:/Users/denis/Desktop/carrega-faixa-cep-uf-localidadehh.php.json')

df_correct = df.to_json('C:/Users/denis/Desktop/MG-TIPOJSONL2323.jl', orient="records", lines=True)