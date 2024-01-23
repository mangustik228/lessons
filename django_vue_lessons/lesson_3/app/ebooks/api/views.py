from rest_framework import generics, mixins
import ebooks.models as M
import ebooks.api.serializiers as S


class EbookListCreateApiView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             generics.GenericAPIView):
    queryset = M.Ebook.objects.all()
    serializer_class = S.EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
