from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Customer, Menu
from .serializers import CustomerSerializer, MenuSerializer
from .services import get_customer_info


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by("name")
    serializer_class = CustomerSerializer

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                customer = serializer.save()
                return Response(
                    {
                        "message": "Customer created successfully",
                        "data": self.serializer_class(customer).data,
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=["get"], url_path="specific")
    def get_specific_customer(self, request):
        try:
            username = request.headers.get("user-name")
            email = request.headers.get("user-email")
            customer = get_customer_info(name=username, email=email)
            if not customer:
                return Response(
                    {"message": "No matching customers found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            print(customer)
            serializer = self.serializer_class(customer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"An error occured {e}", status=500)

    @action(detail=False, methods=["put"], url_path="update")
    def update_customer(self, request):
        try:
            username = request.headers.get("user-name")
            email = request.headers.get("user-email")
            phone_number = request.headers.get("phone-number")
            customer = get_customer_info(name=username, email=email)
            print(customer)
            if username != customer.name:
                customer.name = username
            if email != customer.email:
                customer.email = email
            if phone_number != customer.phone_number:
                customer.phone_number = phone_number

            customer.save()

            serializer = self.serializer_class(customer, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"An error occured {e}", status=500)


class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by("name")
    serializer_class = MenuSerializer
