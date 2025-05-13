

PRETO = "\033[30m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIANO = "\033[36m"
BRANCO = "\033[37m"

PRETO_BRILHANTE = "\033[90m"
VERMELHO_BRILHANTE = "\033[91m"
VERDE_BRILHANTE = "033[92m"
AMARELO_BRILHANTE = "\033[93m"
AZUL_BRILHANTE = "\033[94m"
MAGENTA_BRILHANTE = "\033[95m"
CIANO_BRILHANTE = "\033[96m"
BRANCO_BRILHANTE = "\033[97m"

FUNDO_PRETO = "\033[40m"
FUNDO_VERMELHO = "\033[41m"
FUNDO_VERDE = "\033[42m"
FUNDO_AMARELO = "\033[43m"
FUNDO_AZUL = "\033[44m"
FUNDO_MAGENTA = "\033[45m"
FUNDO_CIANO = "\033[46m"
FUNDO_BRANCO = "033[47m"

RESET = "\033[0m"

def amarelo(texto):
    alt = f"{AMARELO}{texto}{RESET}"
    return alt
    
def verde(texto):
    alt = f"{VERDE}{texto}{RESET}"
    return alt
    
def vermelho(texto):
    alt = f"{VERMELHO}{texto}{RESET}"
    return alt

def vermelhoBrilhante(texto):
    alt = f"{VERMELHO_BRILHANTE}{texto}{RESET}"
    return alt
    