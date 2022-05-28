from dash import Dash, html, dcc, dependencies
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('./dataset/black-friday/BlackFriday.csv')

# GENDER
ages = sorted(df['Age'].unique())
ages.insert(0, 'General')

# AGE
age_ranges = sorted(df['Age'].unique())
age_choices = 2 * age_ranges

# PURCHASE AMOUNTS
dff_uni = df.drop_duplicates(['User_ID'])
male_purchase = dff_uni[dff_uni['Gender'] == 'M']
male_dup = df[df['Gender'] == 'M']

female_purchase = dff_uni[dff_uni['Gender'] == 'F']
female_dup = df[df['Gender'] == 'F']

# CATEGORIES
category = [i for i in range(1, df['Product_Category_1'].max() + 1)]
categories = 2 * category
gender = []
amount = []
for cat in category:
    gender.append('Male')
    amount.append(len(male_dup[male_dup['Product_Category_1'] == cat]) +
                  len(male_dup[male_dup['Product_Category_2'] == cat]) +
                  len(male_dup[male_dup['Product_Category_2'] == cat]))
for cat in category:
    gender.append('Female')
    amount.append(len(female_dup[female_dup['Product_Category_1'] == cat]) +
                  len(female_dup[female_dup['Product_Category_2'] == cat]) +
                  len(female_dup[female_dup['Product_Category_2'] == cat]))


def generate_amount_category():
    amount_category = pd.DataFrame({
        'Category': categories,
        'Amount': amount,
        'Gender': gender
    })
    fig = px.bar(amount_category, x='Category', y='Amount', color='Gender',
                 title='Purchase Amount for Each Category: Total & Gender')
    return fig


app.layout = html.Div([
    html.Div(
        children=[
            html.H1(children='Black Friday Data Analysis Dashboard', style={
                'textAlign': 'center'
            })
        ]
    ),
    html.Div([
        html.H2(children='Gender/Age Proportion Analysis', style={
            'textAlign': 'center'
        }),
        html.Div([
            dcc.Dropdown(
                id='age-ranges',
                options=[{'label': i, 'value': i} for i in ages],
                value='General',
                clearable=False
            ),
            dcc.Graph(id='gender-ratio')

        ],
            style={'width': '49%', 'display': 'inline-block'}
        ),
        html.Div([
            dcc.RadioItems(
                id='genders',
                options=[{'label': i, 'value': i} for i in ['General', 'Male', 'Female']],
                value='General',
                labelStyle={'display': 'inline-block'}
            ),
            dcc.Graph(id='age-ratio')
        ],
            style={'width': '49%', 'display': 'inline-block', 'float': 'right'}
        ),
    ],
        style={
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px'
        }
    ),
    html.Div([
        html.H2(children='Purchase Amount Varying Trend by Age', style={
            'textAlign': 'center'
        }),
        html.Div([
            dcc.RadioItems(
                id='cost-choices',
                options=[{'label': i, 'value': i} for i in ['General', 'Separated Gender']],
                value='General',

            ),
            dcc.Graph(id='cost-varying')
        ]),

    ],
        style={
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px'
        }
    ),
    html.Div([
        html.H2(children='Purchase Amount for Each Category', style={
            'textAlign': 'center'
        }),
        html.Div([
            dcc.Graph(id='amount-category', figure=generate_amount_category())
        ])
    ],
        style={
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px'
        }
    )

]
)


@app.callback(
    dependencies.Output('gender-ratio', 'figure'),
    [
        dependencies.Input('age-ranges', 'value')
    ]
)
def update_gender_ratio(age_range):
    if age_range == 'General':
        dff = df
    else:
        dff = df[df['Age'] == age_range]
    dff = dff.drop_duplicates(['User_ID'])
    male = len(dff[dff['Gender'] == 'M'])
    female = len(dff[dff['Gender'] == 'F'])
    ratio_data = pd.DataFrame({
        'Gender': ['Male', 'Female'],
        'Number': [male, female]
    })
    fig = px.pie(ratio_data, values='Number', names='Gender',
                 title='Gender Proportion by Age: ' + ('General' if age_range == 'General' else 'Age ' + age_range),
                 hole=.3)
    return fig


@app.callback(
    dependencies.Output('age-ratio', 'figure'),
    [
        dependencies.Input('genders', 'value')
    ]
)
def update_age_ratio(gender):
    if gender == 'General':
        dff = df
    else:
        dff = df[df['Gender'] == gender[0]]
    dff = dff.drop_duplicates(['User_ID'])
    res = []
    for age in age_ranges:
        res.append(len(dff[dff['Age'] == age]))
    ratio_data = pd.DataFrame({
        'Age': age_ranges,
        'Number': res
    })
    fig = px.pie(ratio_data, values='Number', names='Age',
                 title='Age Proportion by Gender: ' + gender,
                 hole=.3)
    return fig


@app.callback(
    dependencies.Output('cost-varying', 'figure'),
    [
        dependencies.Input('cost-choices', 'value')
    ]
)
def update_cost_trend(cost_choice):
    res = []
    genders = []
    if cost_choice == 'General':
        for age in age_ranges:
            num_age = len(dff_uni[dff_uni['Age'] == age])
            sum_purchase = len(df[df['Age'] == age])
            res.append(sum_purchase * 1.0 / num_age)
        vary_data = pd.DataFrame({
            'Age': age_ranges,
            'Average Purchase Amount': res

        })
        fig = px.line(vary_data, x='Age', y='Average Purchase Amount', markers=True,
                      title='Purchase Amount Varying by Age: General'
                      )
    else:
        # Male
        for age in age_ranges:
            num_age = len(male_purchase[male_purchase['Age'] == age])
            sum_purchase = len(male_dup[male_dup['Age'] == age])
            res.append(sum_purchase * 1.0 / num_age)
            genders.append('Male')

        # Female
        for age in age_ranges:
            num_age = len(female_purchase[female_purchase['Age'] == age])
            sum_purchase = len(female_dup[female_dup['Age'] == age])
            res.append(sum_purchase * 1.0 / num_age)
            genders.append('Female')
        vary_data = pd.DataFrame({
            'Age': age_choices,
            'Average Purchase Amount': res,
            'Genders': genders
        })
        fig = px.line(vary_data, x='Age', y='Average Purchase Amount', color='Genders', markers=True,
                      title='Purchase Amount Varying by Age: Seperated Gender')

    return fig


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
