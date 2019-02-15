from communicare.core.models import Event


def consts(request):
    return dict(
        PARCELAMENTO="Parcelamento em até 6 vezes",
        TREINAMENTO_ORATORIA={
            "titulo": "Oratória: Comunicação e Expressão."
        },
        CURSO_HIPNOSE={
            "titulo": "Hipnose na Prática"
        },
        TREINAMENTO_INTELIGENCIA_EMOCIONAL={
            "titulo": "Inteligência Emocional"
        },
        ATENDIMENTO_COACHING={
            "titulo": "Coaching"
        },
        ATENDIMENTO_HIPNOTERAPIA={
            "titulo": "Hipnoterapia"
        },
        EVENT_TYPES=Event.EventTypes.__members__,
    )
