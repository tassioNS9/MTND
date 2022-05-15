import time
import json

def readData():
    fData = open('data.json')
    data = json.load(fData)
    fData.close()
    return data

dados = readData()

estds = dados["estds"].split()
alfabeto_Entrada=dados["alfabeto_Entrada"].split() 
alfabeto_Fita = dados["alfabeto_Fita"].split()

divisor = dados["divisor"]
valor_branco = dados["branco"]
qtdTransicoes=int(dados["qtdTransicoes"])
transicoes=dict()
contador = 0

while(contador < qtdTransicoes):
    quintupla = dados["quintuplas"][contador].split()
    key = (quintupla[0], quintupla[1])
    if key not in transicoes:
        transicoes[key]=([[quintupla[2], quintupla[3], quintupla[4]]])
    else:
        transicoes[key].append([quintupla[2], quintupla[3], quintupla[4]])
    contador = contador + 1

estdInicial = dados['estdInicial']
estdsFinais = dados['estdsFinais'].split()
palavras = dados['palavras'].split()
valorAux = 1

for palavra in palavras:
    temp_i = time.perf_counter()
       
    fita=list((divisor+palavra+valor_branco))
    pilha=[(estdInicial, valorAux, fita)]
    aceitacao=False
    while len(pilha)>0:
        p=pilha.pop()
        estdAtual=p[0]
        index_p=p[1]
        fita_p=p[2][:]
        key_p=(estdAtual,fita_p[index_p])
        if key_p not in transicoes and estdAtual in estdsFinais:
            aceitacao=True
            break
        if key_p in transicoes:          
            for a in transicoes[(key_p)]:               
                estdAtual = a[0] 
                fita_p[index_p] = a[1]
                direcionamento = a[2]    
                if direcionamento == 'E':                   
                    pilha.append((estdAtual, index_p-1, fita_p))
                elif direcionamento == 'D':
                    if (index_p+1)==len(fita):
                        fita_p.append(valor_branco)
                    pilha.append((estdAtual, index_p+1, fita_p))
                elif direcionamento == 'P':
                    pilha.append((estdAtual, index_p, fita_p))
    temp_f = time.perf_counter()    
    temp_total=(temp_f-temp_i)*1000

    if aceitacao:
        print("S")
        print(temp_total)
    else:
        print("N")
        print(temp_total)