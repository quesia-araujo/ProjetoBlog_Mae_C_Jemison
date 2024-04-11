from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from noticia.models import Autor, Categoria, Noticia


class NoticiaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["conteudo"].required = False

    class Meta:
        model = Noticia
<<<<<<< Updated upstream
        fields = ['titulo', 'conteudo', 'imagem', 'id_autor', 'id_categoria']
        widgets = {
            'conteudo': CKEditor5Widget(attrs={"class": "django_ckeditor_5", "rows": 10}, config_name='extends')
        }
=======
        fields = ["titulo", "conteudo", "imagem", "id_autor", "id_categoria"]
        widgets = {"conteudo": CKEditor5Widget(config_name="extends")}
>>>>>>> Stashed changes


class CategotiaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["categoria"]


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["autor", "descricao", "data_inicio", "status", "imagem"]
