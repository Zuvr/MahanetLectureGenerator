# MahanetLectureGenerator
A cute little web app that generates random and wild Mahanet lecture topics based on a small database of past lectures.

The project runs on a free Heroku python server using Plotly's Dash (Flask based) framework.

The database contains a list of past lectures and their extracted "templates" and "objects".

The premise of the app is to take a random lecture template (ie: "The history of X") and populate it with a random object (ie: "Baseball bats") to end up with a full lecture title (ie: "The history of Baseball bats").

Due to the complexity of the hebrew language, it is best to stick to objects phrased in their Plural Male form where possible, and templates phrased to support such.
