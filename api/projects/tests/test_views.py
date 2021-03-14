from rest_framework import status
from rest_framework.test import APITestCase

from ..factories import ProjectsFactory


class ProjectListAPIViewTest(APITestCase):
    def setUp(self):
        self.url = '/api/v1/projects/'

    def test_must_to_show_a_project_list(self):
        ProjectsFactory.create_batch(3)

        response = self.client.get(self.url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(3, response.data["count"])
    
    def test_when_there_arent_projects_wont_to_show_a_project_list(self):
        response = self.client.get(self.url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, response.data["count"])
        self.assertEqual([], response.data["results"])

    def test_should_show_all_projects_with_cost_to_be_less_that(self):
        ProjectsFactory.create_batch(2, cost=90)
        ProjectsFactory.create(cost=100)
        ProjectsFactory.create_batch(3, cost=199)

        url = '/api/v1/projects/?min_cost=100'

        response = self.client.get(url)

        self.assertEqual(3, response.data["count"])

    def test_should_show_all_projects_with_cost_to_be_grether_that(self):
        ProjectsFactory.create_batch(2, cost=250)
        ProjectsFactory.create(cost=249)

        url = '/api/v1/projects/?max_cost=250'

        response = self.client.get(url)

        self.assertEqual(2, response.data["count"])
