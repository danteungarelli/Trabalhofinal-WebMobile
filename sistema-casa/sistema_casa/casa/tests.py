from django.test import TestCase
from casa.models import Casa
from django.contrib.auth.models import User

class CasaTestes(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username="testeuser", password="12345")
        self.casa = Casa.objects.create(
            titulo="Casa de Teste",
            num_quartos=2,
            num_banheiros=1,
            tipo=1,  
            area="120",
            status=1, 
            foto=None,
            usuario=self.usuario
        )

    def test_listar_casas(self):
        casas = Casa.objects.all()
        self.assertEqual(len(casas), 1)
        self.assertEqual(casas[0].titulo, "Casa de Teste")
    
    def test_editar_casa(self):
        self.casa.titulo = "Casa Editada"
        self.casa.save()
        self.assertEqual(self.casa.titulo, "Casa Editada")
    
    def test_deletar_casa(self):
        self.casa.delete()
        casas = Casa.objects.all()
        self.assertEqual(len(casas), 0)
