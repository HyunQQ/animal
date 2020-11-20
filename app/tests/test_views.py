from django.test import TestCase


class AnimalViewTest(TestCase):
    def test_response_sido(self):
        response = self.client.get('/sido/')
        self.assertEqual(response.status_code, 200)

    def test_response_sigungu(self):
        response = self.client.get('/sigungu/?upr_cd=6110000')
        self.assertEqual(response.status_code, 200)

    def test_response_shelter(self):
        response = self.client.get('/shelter/?upr_cd=6110000&org_cd=3220000')
        self.assertEqual(response.status_code, 200)

    def test_response_shelter_detail(self):
        response = self.client.get('/shelter_detail/?care_reg_no=311322200900001')
        self.assertEqual(response.status_code, 200)

    def test_response_kind(self):
        response = self.client.get('/kind/?up_kind_cd=417000')
        self.assertEqual(response.status_code, 200)

    def test_response_abandonment(self):
        response = self.client.get('/abandonment/?numOfRows=10&pageNo=1&bgnde=20140601&endde=20140630&upkind=417000&kind=000054&upr_cd=6110000&org_cd=3220000&care_reg_no=311322200900001&state=notice&neuter_yn=Y')
        self.assertEqual(response.status_code, 200)



