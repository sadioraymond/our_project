from django.db import models

# Create your models here.
class Abonnement(models.Model):
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    id_structure = models.ForeignKey('Structure', models.DO_NOTHING, db_column='id_structure')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'abonnement'


class Administrateur(models.Model):
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    id_structure = models.ForeignKey('Structure', models.DO_NOTHING, db_column='id_structure')
    datedeb = models.DateField()
    datefin = models.DateField()

    class Meta:
        managed = False
        db_table = 'administrateur'


class Article(models.Model):
    nom = models.CharField(max_length=30)
    id_type = models.ForeignKey('TypeArticle', models.DO_NOTHING, db_column='id_type')

    class Meta:
        managed = False
        db_table = 'article'


class BoiteAIdee(models.Model):
    libelle = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'boite_a_idee'


class Commentaire(models.Model):
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    id_pub = models.ForeignKey('Publication', models.DO_NOTHING, db_column='id_pub', blank=True, null=True)
    id_event = models.ForeignKey('Evenement', models.DO_NOTHING, db_column='id_event', blank=True, null=True)
    id_faq = models.ForeignKey('Faq', models.DO_NOTHING, db_column='id_faq', blank=True, null=True)
    contenu = models.TextField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'commentaire'


class DetailAcces(models.Model):
    id_admin = models.ForeignKey(Administrateur, models.DO_NOTHING, db_column='id_admin')
    id_droit = models.ForeignKey('DroitDAcces', models.DO_NOTHING, db_column='id_droit')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'detail_acces'


class DetailArticle(models.Model):
    id_struct = models.ForeignKey('Structure', models.DO_NOTHING, db_column='id_struct')
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='id_article')
    prix = models.FloatField()
    date_art = models.DateField()

    class Meta:
        managed = False
        db_table = 'detail_article'


class DetailEvenement(models.Model):
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    id_evenement = models.ForeignKey('Evenement', models.DO_NOTHING, db_column='id_evenement')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'detail_evenement'


class DetailSession(models.Model):
    tache = models.CharField(max_length=30)
    time = models.DateTimeField()
    id_session = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detail_session'


class DetailUtilisateur(models.Model):
    id_utilisateur = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_utilisateur')
    id_type = models.ForeignKey('TypeUtilisateur', models.DO_NOTHING, db_column='id_type')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'detail_utilisateur'


class DroitDAcces(models.Model):
    libelle = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'droit_d_acces'


class Evenement(models.Model):
    description = models.CharField(max_length=50)
    nom = models.CharField(max_length=30)
    contenu = models.TextField()
    id_type = models.ForeignKey('TypeEvenement', models.DO_NOTHING, db_column='id_type')
    id_admin = models.ForeignKey(Administrateur, models.DO_NOTHING, db_column='id_admin')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'evenement'


class Faq(models.Model):
    contenu = models.TextField()
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'faq'


class Idee(models.Model):
    conteu = models.TextField()
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    id_boite = models.ForeignKey(BoiteAIdee, models.DO_NOTHING, db_column='id_boite')

    class Meta:
        managed = False
        db_table = 'idee'


class NoteArticle(models.Model):
    id_detail = models.ForeignKey(DetailArticle, models.DO_NOTHING, db_column='id_detail')
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    note = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'note_article'


class NoteStructure(models.Model):
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    id_structe = models.ForeignKey('Structure', models.DO_NOTHING, db_column='id_structe')
    note = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'note_structure'


class Notification(models.Model):
    id_pub = models.ForeignKey('Publication', models.DO_NOTHING, db_column='id_pub', blank=True, null=True)
    id_event = models.ForeignKey(Evenement, models.DO_NOTHING, db_column='id_event', blank=True, null=True)
    id_comm = models.ForeignKey(Commentaire, models.DO_NOTHING, db_column='id_comm', blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'notification'


class Publication(models.Model):
    contenu = models.TextField()
    id_structure = models.ForeignKey('Structure', models.DO_NOTHING, db_column='id_structure')
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'publication'


class Session(models.Model):
    datedeb = models.DateField()
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    datefin = models.DateField()

    class Meta:
        managed = False
        db_table = 'session'


class SousStructure(models.Model):
    libelle = models.CharField(max_length=30)
    id_struct = models.ForeignKey('Structure', models.DO_NOTHING, db_column='id_struct')
    id_type = models.ForeignKey('TypeStructure', models.DO_NOTHING, db_column='id_type')

    class Meta:
        managed = False
        db_table = 'sous_structure'


class Structure(models.Model):
    nom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=30)
    localisation = models.FloatField()
    id_user = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_user')
    tel = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    id_type = models.ForeignKey('TypeStructure', models.DO_NOTHING, db_column='id_type')

    class Meta:
        managed = False
        db_table = 'structure'


class TypeArticle(models.Model):
    libelle = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'type_article'


class TypeEvenement(models.Model):
    libelle = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'type_evenement'


class TypeStructure(models.Model):
    libelle = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'type_structure'


class TypeUtilisateur(models.Model):
    libelle = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'type_utilisateur'


class Utilisateur(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=55)
    login = models.CharField(max_length=30)
    mdp = models.CharField(max_length=20)
    date_naiss = models.DateField()
    adresse = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'utilisateur'
