from django.db import models


class Project(models.Model):
    title = models.CharField(
        verbose_name='Project title', max_length=500, null=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(verbose_name='Project category', choices=[
                                ('0', 'Residential'), ('1', 'Commercial'), ('2', 'Institutional'), ('3', 'Others')], max_length=1)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    @property
    def images(self):
        return ProjectImage.objects.filter(project=self)

    @property
    def thumb(self):
        return self.images[0].image.url

    @property
    def small_description(self):
        if len(self.description) > 200:
            return self.description[:247]+'...'
        return self.description


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_gallery')
    category = models.CharField(verbose_name='Image category', choices=[
                                ('0', 'Indoor'), ('1', 'Outdoor'), ('2', 'Top view')], max_length=1)


class ContactUs(models.Model):
    name = models.CharField(verbose_name='Name',
                            max_length=200, null=False, default='')
    contact = models.CharField(
        verbose_name='Contact (Phone/Email)', max_length=300, null=False, default='')
    date_time = models.DateTimeField(
        verbose_name='Date and time', auto_now_add=True)
    message = models.TextField(verbose_name='Message')

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class Review(models.Model):
    img = models.ImageField(verbose_name='Client Image',
                            upload_to="user_img/", null=False)
    name = models.CharField(max_length=100, null=False)
    review = models.TextField()
