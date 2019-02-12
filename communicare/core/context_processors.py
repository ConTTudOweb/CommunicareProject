from communicare.core.models import Event


def consts(request):
    return dict(
        PARCELAMENTO="Parcelamento em até 10 vezes",
        TREINAMENTO_ORATORIA={
            "titulo": "Oratória: Comunicação e Expressão."
        },
        CURSO_HIPNOSE={
            "titulo": "Hipnose na Prática"
        },
        TREINAMENTO_INTELIGENCIA_EMOCIONAL={
            "titulo": "Inteligência Emocional"
        },
        EVENT_TYPES=Event.EventTypes.__members__,
    )
