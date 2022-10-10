import pandas as pd
import random

def Importar_dados():
    df = pd.read_csv('https://raw.githubusercontent.com/digitalinnovationone/live-coding-evitando-o-7x1-com-python-e-sql/main/data.csv')
    return df

class Selecao:
  MELHOR_PONTUA = 1837.6
  FAVori = ['ING','ARG','FRA','ALE','BRA']
  def __init__(self, data):
    dataset = data.split('|')
    self.name = dataset[0]
    self.score = float(dataset[1])

  def motivacao(self):

    self.lastmotivation = random.uniform(65,(100*self.score)/Selecao.MELHOR_PONTUA)
    if self.lastmotivation <= 98 and self.name in Selecao.FAVori:
      self.lastmotivation += 2
    return self.lastmotivation

def Fase_de_grupo(df):
  melhoretimespor_grupo = {}

  for label, content in df.items():
    time1 = Selecao(content[0])
    time2 = Selecao(content[1])
    time3 = Selecao(content[2])
    time4 = Selecao(content[3])
    melhoretimespor_grupo[label] = sorted([time1,time2,time3,time4],key=Selecao.motivacao,reverse=True)
  return melhoretimespor_grupo

def Exibir_resultado_fase_grupo(diciona):
  print('---'*20)
  print('Resultados da fase de grupos:')
  for grupo, timesmotivados in diciona.items():
    print(f'Grupo {grupo}: ',end='')
    for time in timesmotivados:
      print(f'{time.name} ({time.lastmotivation:.2f}) ', end='')
    print()

# Classifica as 2 melhores seleções de cada grupo:
def Classificados_to_oitavas(classif):
  grupos = classif.keys()
  classificados = {}
  for g in grupos:
    for i in range(2):
      classificados[f'time{i+1}{g}'] = classif[g][i]
  return classificados


def Confrontos_oitavas(times):

  quartas = {}
  quartas['quarta1'] = times['time1A'] if times['time1A'].motivacao() > times['time2B'].motivacao() else times['time2B']
  quartas['quarta2'] = times['time1C'] if times['time1C'].motivacao() > times['time2D'].motivacao() else times['time2D']
  quartas['quarta3'] = times['time1E'] if times['time1E'].motivacao() > times['time2F'].motivacao() else times['time2F']
  quartas['quarta4'] = times['time1G'] if times['time1G'].motivacao() > times['time2H'].motivacao() else times['time2H']
  quartas['quarta5'] = times['time1B'] if times['time1B'].motivacao() > times['time2A'].motivacao() else times['time2A']
  quartas['quarta6'] = times['time1D'] if times['time1D'].motivacao() > times['time2C'].motivacao() else times['time2C']
  quartas['quarta7'] = times['time1F'] if times['time1F'].motivacao() > times['time2E'].motivacao() else times['time2E']
  quartas['quarta8'] = times['time1H'] if times['time1H'].motivacao() > times['time2G'].motivacao() else times['time2G']

  print('\n','Resultados das Oitavas de finais:')
  print(f"  {times['time1A'].name} ({times['time1A'].lastmotivation:.2f}) x {times['time2B'].name} ({times['time2B'].lastmotivation:.2f})")
  print(f"  {times['time1C'].name} ({times['time1C'].lastmotivation:.2f}) x {times['time2D'].name} ({times['time2D'].lastmotivation:.2f})")
  print(f"  {times['time1E'].name} ({times['time1E'].lastmotivation:.2f}) x {times['time2F'].name} ({times['time2F'].lastmotivation:.2f})")
  print(f"  {times['time1G'].name} ({times['time1G'].lastmotivation:.2f}) x {times['time2H'].name} ({times['time2H'].lastmotivation:.2f})")
  print(f"  {times['time1B'].name} ({times['time1B'].lastmotivation:.2f}) x {times['time2A'].name} ({times['time2A'].lastmotivation:.2f})")
  print(f"  {times['time1D'].name} ({times['time1D'].lastmotivation:.2f}) x {times['time2C'].name} ({times['time2C'].lastmotivation:.2f})")
  print(f"  {times['time1F'].name} ({times['time1F'].lastmotivation:.2f}) x {times['time2E'].name} ({times['time2E'].lastmotivation:.2f})")
  print(f"  {times['time1H'].name} ({times['time1H'].lastmotivation:.2f}) x {times['time2G'].name} ({times['time2G'].lastmotivation:.2f})")

  return quartas


def Confrontos_quartas(times):

  semis = {}
  semis['semi1'] = times['quarta1'] if times['quarta1'].motivacao() > times['quarta2'].motivacao() else times['quarta2']
  semis['semi2'] = times['quarta3'] if times['quarta3'].motivacao() > times['quarta4'].motivacao() else times['quarta4']
  semis['semi3'] = times['quarta5'] if times['quarta5'].motivacao() > times['quarta6'].motivacao() else times['quarta6']
  semis['semi4'] = times['quarta7'] if times['quarta7'].motivacao() > times['quarta8'].motivacao() else times['quarta8']

  print('\n','Resultados das Quartas de finais:')
  print(f"  {times['quarta1'].name} ({times['quarta1'].lastmotivation:.2f}) x {times['quarta2'].name} ({times['quarta2'].lastmotivation:.2f})")
  print(f"  {times['quarta3'].name} ({times['quarta3'].lastmotivation:.2f}) x {times['quarta4'].name} ({times['quarta4'].lastmotivation:.2f})")
  print(f"  {times['quarta5'].name} ({times['quarta5'].lastmotivation:.2f}) x {times['quarta6'].name} ({times['quarta6'].lastmotivation:.2f})")
  print(f"  {times['quarta7'].name} ({times['quarta7'].lastmotivation:.2f}) x {times['quarta8'].name} ({times['quarta8'].lastmotivation:.2f})")

  return semis


def Confrontos_semis(times):

  finais = {}
  finais['final1'] = times['semi1'] if times['semi1'].motivacao() > times['semi2'].motivacao() else times['semi2']
  finais['terceiro1'] = times['semi2'] if times['semi1'].lastmotivation > times['semi2'].lastmotivation else times['semi1']
  finais['final2'] = times['semi3'] if times['semi3'].motivacao() > times['semi4'].motivacao() else times['semi4']
  finais['terceiro2'] = times['semi4'] if times['semi3'].lastmotivation > times['semi4'].lastmotivation else times['semi3']

  print('\n','Resultados das Semi-finais:')
  print(f"  {times['semi1'].name} ({times['semi1'].lastmotivation:.2f}) x {times['semi2'].name} ({times['semi2'].lastmotivation:.2f})")
  print(f"  {times['semi3'].name} ({times['semi3'].lastmotivation:.2f}) x {times['semi4'].name} ({times['semi4'].lastmotivation:.2f})")

  return finais


def Finais(jogos):

  campeao = jogos['final1'] if jogos['final1'].motivacao() > jogos['final2'].motivacao() else jogos['final2']
  second = jogos['final2'] if jogos['final1'].lastmotivation > jogos['final2'].lastmotivation else jogos['final1']

  terceiro = jogos['terceiro1'] if jogos['terceiro1'].motivacao() > jogos['terceiro2'].motivacao() else jogos['terceiro2']
  quarto = jogos['terceiro2'] if jogos['terceiro1'].lastmotivation > jogos['terceiro2'].lastmotivation else jogos['terceiro1']

  print('\n','Resultados da Final e disputa do Terceiro lugar:')
  print(f'   Campeão: {campeao.name} ({campeao.lastmotivation:.2f})')
  print(f'   2º: {second.name} ({second.lastmotivation:.2f})')
  print(f'   3º: {terceiro.name} ({terceiro.lastmotivation:.2f})')
  print(f'   4º: {quarto.name} ({quarto.lastmotivation:.2f})')