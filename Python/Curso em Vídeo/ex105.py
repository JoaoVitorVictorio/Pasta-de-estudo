# Analisando e gerando Dicionários
def notas(*num, sit=False):
    """
    -> Função p/ analisar notas de vários alunos
    :param num: Uma ou mais notas de alunos
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma
    """
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num)/len(num)
    if sit:
        if r['média'] > 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
        return r


resp = notas(5.5, 6.5, 9, 8.5, sit=True)
print(resp)
help(notas)
