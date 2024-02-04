from django.db import models

class CollegeEssay(models.Model):
    college_name = models.CharField(max_length=255, verbose_name='College Name')
    major = models.CharField(max_length=100, verbose_name='Intended Major')

    original_essay_title = models.CharField(max_length=255, verbose_name='Original Essay Title')
    original_essay_content = models.TextField(verbose_name='Original Essay Content')

    # Add default value or allow null for the following fields
    improved_essay_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Improved Essay Title')
    additional_notes = models.TextField(blank=True, null=True, verbose_name='Additional Notes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.college_name} - {self.major} - {self.original_essay_title}"

    class Meta:
        verbose_name_plural = 'College Essays'