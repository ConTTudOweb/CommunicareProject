from communicare.core.models import Event

EMPRESA_DESCRICAO = "Nosso propósito é mediar o conhecimento, potencializando o desenvolvimento pessoal, promovendo " \
                    "a expressão do ser, trazendo a força e o poder para superar os desafios cotidianos e atingir " \
                    "patamares ainda maiores."
TREINAMENTO_ORATORIA_TITULO = "Oratória: Comunicação e Expressão."
TREINAMENTO_ORATORIA_RESUMO = "Um treinamento que envolve técnicas de oratória e programação neurolinguística (PNL) buscando entender e compreender todos os sentimentos que nos sabotam diante de uma apresentação"
CURSO_HIPNOSE_TITULO = "Hipnose na Clínica"
CURSO_HIPNOSE_RESUMO = "Um curso que alinha teoria à prática, desmistificando o que é hipnose e compreendendo seu real fundamento terapêutico para cura de traumas e fobias"
TREINAMENTO_INTELIGENCIA_EMOCIONAL_TITULO = "Inteligência Emocional"
TREINAMENTO_INTELIGENCIA_EMOCIONAL_RESUMO = "Saiba como lidar com suas emoções neste treinamento através da prática da Inteligência Emocional e obtenha os resultados que você busca em sua vida pessoal e profissional"
ATENDIMENTO_COACHING_TITULO = "Coaching"
ATENDIMENTO_COACHING_RESUMO = "Uma metodologia extraordinária que tem como finalidade descobrir soluções que auxiliem as pessoas a alcançarem suas metas e potencializar resultados"
ATENDIMENTO_HIPNOTERAPIA_TITULO = "Hipnoterapia"
ATENDIMENTO_HIPNOTERAPIA_RESUMO = "A utilização da Hipnose na terapia, possibilita de maneira consistente, identificar e modificar a estrutura da realidade de cada indivíduo. Ajudando a aumentar a confiança,  construindo resultados extraordinários, tratando medos/fobias e retomando o prazer pela vida"
PALESTRA_INTELIGENCIA_EMOCIONAL_TITULO = "Inteligência Emocional"
PALESTRA_INTELIGENCIA_EMOCIONAL_RESUMO = "Aprenda um pouco mais sobre suas emoções nesta palestra através da prática da Inteligência Emocional e obtenha os resultados que você busca em sua vida pessoal e profissional"

KEYWORDS = \
    "a communicare é confiavel?, communicare treinamentos, communicare treinamentos apucarana, cursos em apucarana, " \
    "curso em apucarana, treinamentos em apucarana, treinamento em apucarana, palestras em apucarana, " \
    "palestra em apucarana, pnl, programação neurolinguística, apucarana, vinicius campos, alessandro folk"
KEYWORDS_TREINAMENTO_ORATORIA = \
    "curso de oratória, treinamento de oratória, curso de comunicação, treinamento de comunicação, " \
    "curso de oratória em apucarana, curso de comunicação em apucarana, treinamento de oratória em apucarana, " \
    "treinamento de comunicação em apucarana, medo de falar em público, aprenda a falar em público, " \
    "perca o medo de falar em público, como falar em público, aprenda a fazer um discurso, como fazer um discurso, " \
    "apresentação de tcc, como falar em público e encantar pessoas, oratória, comunicação, medo de falar em público"
KEYWORDS_CURSO_HIPNOSE = \
    "curso de hipnose, treinamento de hipnose, curso de hipnose em apucarana, treinamento de hipnose em apucarana, " \
    "auto controle, aprenda a hipnotizar, como hipnotizar pessoas, hipnose, mente consciente, mente subconsciente, " \
    "mente inconsciente, o que é mente consciente, o que é mente inconsciente, o que é mente subconsciente, " \
    "hipnose clínica, hipnose clinica"
KEYWORDS_INTELIGENCIA_EMOCIONAL = \
    "o que é inteligência emocional?, inteligência emocional, viver em paz, viver feliz, gestão da emoção, " \
    "controle da emoção, como eliminar ansiedade, como acabar com a depressão, tenho depressão, depressão, " \
    "como se motivar, o que é motivação, como saber se relacionar, como conhecer as emoções, " \
    "como controlar as emoções, como controlar a raiva, como controlar o ódio, como controlar a pornografia, " \
    "como controlar o medo, como reduzir emoções negativas, como ser mais positivo, como diminuir o stress, " \
    "empatia, como praticar a empatia, mente consciente, mente subconsciente, mente inconsciente"
KEYWORDS_TREINAMENTO_INTELIGENCIA_EMOCIONAL = \
    "curso de inteligência emocional, treinamento de inteligência emocional, " \
    "curso de inteligência emocional em apucarana, treinamento de inteligência emocional em apucarana, " + \
    KEYWORDS_INTELIGENCIA_EMOCIONAL
KEYWORDS_ATENDIMENTO_COACHING = \
    "atendimento de coaching, atendimento coaching, atendimento de coach, atendimento coach, curso de coaching" \
    "acompanhamento de carreira, atendimento coaching em apucarana, coaching em apucarana, life coach, leader coach, " \
    "como evoluir na vida pessoal, como evoluir na carreira, como ser mais proativo, como ser mais comunicativo, " \
    "como ter mais sucesso, acompanhamento de coaching, professional coach, coaching, eneagrama"
KEYWORDS_ATENDIMENTO_HIPNOTERAPIA = \
    "atendimento hipnoterapia em apucarana, atendimento de hipnoterapia em apucarana, atendimento de hipnoterapia, " \
    "atendimento em hipnose, hipnose clínica, tratar fobias, tratar traumas, tratar depressão, tratar medos" \
    "tratar medo de falar em público, tratar ansiedade, como tratar fobias, como tratar medos, como tratar traumas, " \
    "como tratar depressão, como tratar ansiedade, atendimento hipnose em apucarana, hipnoterapia em apucarana, hipnose"
KEYWORDS_PALESTRA_INTELIGENCIA_EMOCIONAL = \
    "palestra de inteligência emocional, palestra de inteligência emocional em apucarana, " + \
    KEYWORDS_INTELIGENCIA_EMOCIONAL

PAGES = dict(
    PAGE_HOME={
        "title": "Centro de Treinamentos em Excelência Humana",
        "description": EMPRESA_DESCRICAO,
        "keywords": "%s, %s, %s, %s, %s, %s" % (
            KEYWORDS, KEYWORDS_TREINAMENTO_ORATORIA, KEYWORDS_CURSO_HIPNOSE,
            KEYWORDS_TREINAMENTO_INTELIGENCIA_EMOCIONAL, KEYWORDS_ATENDIMENTO_COACHING,
            KEYWORDS_ATENDIMENTO_HIPNOTERAPIA
        )
    },
    PAGE_TREINAMENTO_ORATORIA={
        "title": TREINAMENTO_ORATORIA_TITULO,
        "description": TREINAMENTO_ORATORIA_RESUMO,
        "keywords": "%s, %s" % (KEYWORDS, KEYWORDS_TREINAMENTO_ORATORIA)
    },
    PAGE_CURSO_HIPNOSE={
        "title": CURSO_HIPNOSE_TITULO,
        "description": CURSO_HIPNOSE_RESUMO,
        "keywords": "%s, %s" % (KEYWORDS, KEYWORDS_CURSO_HIPNOSE)
    },
    PAGE_TREINAMENTO_INTELIGENCIA_EMOCIONAL={
        "title": TREINAMENTO_INTELIGENCIA_EMOCIONAL_TITULO,
        "description": TREINAMENTO_INTELIGENCIA_EMOCIONAL_RESUMO,
        "keywords": "%s, %s" % (
            KEYWORDS, KEYWORDS_TREINAMENTO_INTELIGENCIA_EMOCIONAL)
    },
    PAGE_ATENDIMENTO_COACHING={
        "title": ATENDIMENTO_COACHING_TITULO,
        "description": ATENDIMENTO_COACHING_RESUMO,
        "keywords": "%s, %s" % (KEYWORDS, KEYWORDS_ATENDIMENTO_COACHING)
    },
    PAGE_ATENDIMENTO_HIPNOTERAPIA={
        "title": ATENDIMENTO_HIPNOTERAPIA_TITULO,
        "description": ATENDIMENTO_HIPNOTERAPIA_RESUMO,
        "keywords": "%s, %s" % (KEYWORDS, KEYWORDS_ATENDIMENTO_HIPNOTERAPIA)
    },
    PAGE_PALESTRA_INTELIGENCIA_EMOCIONAL={
        "title": PALESTRA_INTELIGENCIA_EMOCIONAL_TITULO,
        "description": PALESTRA_INTELIGENCIA_EMOCIONAL_RESUMO,
        "keywords": "%s, %s" % (
            KEYWORDS, KEYWORDS_PALESTRA_INTELIGENCIA_EMOCIONAL)
    },
    PAGE_GENERICA={
        "title": "Centro de Treinamentos em Excelência Humana",
        "description": EMPRESA_DESCRICAO
    }
)

CONSTS = dict(
    EMPRESA={
        "name": "Communicare Treinamentos",
    },
    SITE={
        "url": "https://communicaretreinamentos.com.br"
    },
    PARCELAMENTO="",
    TREINAMENTO_ORATORIA={
        "titulo": TREINAMENTO_ORATORIA_TITULO,
        "resumo": "%s (...)" % TREINAMENTO_ORATORIA_RESUMO
    },
    CURSO_HIPNOSE={
        "titulo": CURSO_HIPNOSE_TITULO,
        "resumo": "%s (...)" % CURSO_HIPNOSE_RESUMO
    },
    TREINAMENTO_INTELIGENCIA_EMOCIONAL={
        "titulo": TREINAMENTO_INTELIGENCIA_EMOCIONAL_TITULO,
        "resumo": "%s (...)" % TREINAMENTO_INTELIGENCIA_EMOCIONAL_RESUMO
    },
    ATENDIMENTO_COACHING={
        "titulo": ATENDIMENTO_COACHING_TITULO,
        "resumo": "%s (...)" % ATENDIMENTO_COACHING_RESUMO
    },
    ATENDIMENTO_HIPNOTERAPIA={
        "titulo": ATENDIMENTO_HIPNOTERAPIA_TITULO,
        "resumo": "%s (...)" % ATENDIMENTO_HIPNOTERAPIA_RESUMO
    },
    PALESTRA_INTELIGENCIA_EMOCIONAL={
        "titulo": PALESTRA_INTELIGENCIA_EMOCIONAL_TITULO,
        "resumo": PALESTRA_INTELIGENCIA_EMOCIONAL_RESUMO
    },
    EVENT_TYPES=Event.EventTypes.__members__,
)


def consts(request):
    return CONSTS
