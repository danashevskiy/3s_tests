import pytest
from pages.calendar_constructor import CalendarConstructor
from settings import BASE_URL


class TestCalendar:
    @pytest.mark.parametrize(
        "test_user",
        [
            {
                "subject": 'Выбрать все',
                "country": 'Выбрать все',
                "width": '230',
                "height": '240'
            },
            {
                "subject": 'Выбрать все',
                "country": 'Выбрать все',
                "width": '1020',
                "height": '720'
            },
            {
                "subject": 'Выбрать все',
                "country": 'Выбрать все',
                "width": '',
                "height": ''
            },
        ],
        ids=["minimum_size_generation",
             "maximum_size_generation",
             "full_window_generation"
            ]
    )
    def test_cal_const(
        self,
        test_cal_const: CalendarConstructor,
        test_user: dict
    ):
        #test_cal_const.visit(BASE_URL)
        
        test_cal_const.cal_form.choose_subject(test_user['subject'])
        test_cal_const.cal_form.choose_country(test_user['country'])
        if test_user['width'] and test_user['height']:
            test_cal_const.cal_form.width_input.fill(test_user['width'])
            test_cal_const.cal_form.height_input.fill(test_user['height'])
        else:
            test_cal_const.cal_form.radio_width.click()
            test_cal_const.cal_form.radio_height.click()
        test_cal_const.cal_form.radio_blue.click()
        test_cal_const.cal_form.generate.click()
        test_cal_const.cal_form.generate.should_be_visible()
        
