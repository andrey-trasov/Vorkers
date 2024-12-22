from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView


from vorkers.models import Vorkers
from vorkers.serializers import VorkersSerializer


class VorkersRetrieveAPIView(RetrieveAPIView):
    """
    Возвращает описание мастера
    """

    queryset = Vorkers.objects.all()
    serializer_class = VorkersSerializer


class TeamVorkersListAPIView(ListAPIView):
    """
    Возвращает список работников в бригаде
    """

    serializer_class = VorkersSerializer

    def get_queryset(self):
        team_id = self.kwargs.get("team_id", None)
        if team_id is not None:
            return Vorkers.objects.filter(team_number=team_id)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
