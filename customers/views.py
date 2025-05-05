from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
    
    # def get_queryset(self):
    #     return Customer.objects.none()
    
    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
    #         return [IsAdminUser()]
    #     return super().get_permissions()
    
    @action(detail=False, methods=['get', 'put', 'patch'], permission_classes=[IsAuthenticated])
    def me(self, request):
        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            # Jika profil belum ada, buat baru
            customer = Customer.objects.create(user=request.user)
        
        if request.method == 'GET':
            serializer = self.get_serializer(customer)
            return Response(serializer.data)
        
        serializer = self.get_serializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
    def create(self, request, *args, **kwargs):
        # Menonaktifkan create dengan mengembalikan response error
        return Response({"detail": "Create operation is disabled."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        # Menonaktifkan update dengan mengembalikan response error
        return Response({"detail": "Update operation is disabled."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        # Menonaktifkan delete dengan mengembalikan response error
        return Response({"detail": "Delete operation is disabled."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
    def partial_update(self, request, *args, **kwargs):
        # Menonaktifkan partial update dengan mengembalikan response error
        return Response({"detail": "Partial update operation is disabled."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)