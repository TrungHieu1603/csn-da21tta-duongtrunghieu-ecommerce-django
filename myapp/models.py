from django.db import models


class Resume(models.Model):
  
    Ho_Ten = models.CharField(max_length=100)
    email = models.EmailField()
    So_Dien_Thoai = models.CharField(max_length=20)
    Tom_Tat = models.TextField()
    Kinh_Nghiem = models.TextField()
    Giao_Duc = models.TextField()
    Giao_Duc2 = models.CharField(max_length=100, default='Trung Học Cơ Sở Thị Trấn Cầu Ngang')
    Giao_Duc3 = models.CharField(max_length=100, default='Trung Tâm GDNN & GDTX huyện Cầu Ngang')
    Ky_Nang = models.TextField()
    
    def __str__(self):
        return self.Ho_Ten
