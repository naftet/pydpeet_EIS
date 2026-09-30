# ruff: noqa
# Auto-generated test placeholder file
# Fill in real tests and remove or adjust placeholders


class Test__unix_time_to_datetime_df(object):
    """Placeholder failing test for variable 'df' of '_unix_time_to_datetime'."""

    def test_placeholder(self):
        raise NotImplementedError("Test not implemented for variable: df of _unix_time_to_datetime")


# import pandas as pd

# from pydpeet.io.utils.formatter_utils import _unix_time_to_datetime


# class Test__unix_time_to_datetime_df(object):
#     def test_converts_unix_seconds_and_coerces_invalid_values(self):
#         df = pd.DataFrame(
#             {
#                 "Date_Time": [0, 1_700_000_000, "invalid", None],
#                 "Other": [1, 2, 3, 4],
#             }
#         )

#         result = _unix_time_to_datetime(df)

#         expected = pd.DataFrame(
#             {
#                 "Date_Time": [
#                     pd.Timestamp("1970-01-01 00:00:00"),
#                     pd.Timestamp("2023-11-14 22:13:20"),
#                     pd.NaT,
#                     pd.NaT,
#                 ],
#                 "Other": [1, 2, 3, 4],
#             }
#         )
#         expected["Date_Time"] = expected["Date_Time"].astype("datetime64[ns]")
#         pd.testing.assert_frame_equal(result, expected)
