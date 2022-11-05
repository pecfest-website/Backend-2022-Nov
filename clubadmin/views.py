from functools import partial

from events.models import Event
from events.serializers import EventSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

# Create your views here.


class EventAPIView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def post(self, request):
        data = request.data
        club = request.user.club
        data["club"] = club.id  # add club id to the data
        serializer = self.get_serializer(data=data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()  # save event

        response_data = {"message": "Event created"}
        response_data["event_id"] = serializer.data["id"]
        return Response(response_data, status.HTTP_201_CREATED)

    def delete(self, request, event_id, *args, **kwargs):
        try:
            event = self.get_queryset().get(id=event_id)
        except:
            return Response(
                {"error": "event does not exists"}, status.HTTP_404_NOT_FOUND
            )  # return error if event doesn't exists

        event.delete()
        response_data = {"message": "event deleted"}
        return Response(response_data, status.HTTP_200_OK)

    def patch(self, request, event_id, *args, **kwargs):
        data = request.data
        club = request.user.club
        data["club"] = club.id  # add club id to the data

        try:
            event = self.get_queryset().get(
                id=event_id
            )  # fetch the event to be modified
        except:
            return Response(
                {"error": "event does not exists"}, status.HTTP_404_NOT_FOUND
            )  # return error if event doesn't exists

        # verify if the user and event belong to the same club
        if str(event.club_id) != str(club.id):
            return Response({"error": "access denied"}, status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(
            event, data=data, context={"user": request.user}, partial=True
        )  # create serializer
        serializer.is_valid(raise_exception=True)
        serializer.save()  # update

        response_data = {"message": "Event modified"}
        response_data["event_id"] = event_id
        return Response(response_data, status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
<<<<<<< HEAD
        club_id = kwargs.get("club_id")
        try:
            event_objs = Event.objects.filter(club_id=club_id)
        except Exception:
            return Response(
                {"message": "Invalid club id"}, status=status.HTTP_400_BAD_REQUEST
            )
        if event_objs:
            serializer = EventSerializer(event_objs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Invalid club id"}, status=status.HTTP_400_BAD_REQUEST
            )


class ParticipantsAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    # utility function to return list of users in a team -> works for both team and individual event
    def get_participants_json_from_team(self, t):
        participants = []
        for u in list(t.user.all()):
            participant = {
                "user_id":u.user.id,
                "first_name":u.user.first_name,
                "last_name":u.user.last_name,
                "email":u.user.email,
            }
            for d in list(u.user.details.all()):
                participant['college'] = d.college

            participants.append(participant)

        return participants
            

    def get(self, request, event_id, *args, **kwargs):
        
        club = "b509e6a7-42f8-4626-8e67-fa6aa5e023ba" # need to get from user_id which is club admin id
        try:
            event = self.get_queryset().get(id = event_id)
        except:
            return Response({"error":"event does not exist"})

        if str(event.club.id) != club:
            return Response({"error":"access denied"}, status.HTTP_401_UNAUTHORIZED)
        
        if event.type == "INDIVIDUAL":
            teams = list(event.teamsregistered.all())
            response_data = []
            for t in teams:
                participants = self.get_participants_json_from_team(t)
                response_data.append(participants)
        
        else:
            teams = list(event.teamsregistered.all())
            response_data = []
            for t in teams:
                if t.is_registered:
                    team = {"team_name":t.name}
                    participants = self.get_participants_json_from_team(t)
                    team['members'] = participants
                    response_data.append(team)
                
        res = {"event_type":event.type, "data":response_data}  
        
        return Response(res, status.HTTP_200_OK)

    
        
=======
        club_id = request.user.club_id
        event_objs = Event.objects.filter(club_id=club_id)
        serializer = EventSerializer(event_objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
>>>>>>> main
