### Problem Specifics:
The target regressor D is the initial level of the country's wealth.ThecontrolsWincludemeasuresofeducationlevels,qualityofinstitutions,tradeopenness and political stability in the country.The dataset contains 90 countries and about 60 controls.So ‘P’ is approximately 60, and the ‘N’ is 90, a relatively small number.P/N is hence not very small.

This means that we are operating in a high-dimensional setting.Therefore,we expect the least-squares method to provide a poor,very noisy estimate

### Dataset
The dataset contains growth data of Barro-Lee. The Barro Lee data consists of a panel of 138 countries for the period 1960 to 1985. The dependent variable is national growth rates in GDP per capita for the periods 1965-1975 and 1975-1985. The growth rate in GDP over a period from t1 to t2 is commonly defined as log(GDPt1 /GDPt2 ). The number of variables are p=62. The number of complete observations is n=90.

The full data set and further details can be found at http://www.nber.org/pub/barro.lee, http: //www.barrolee.com, and, http://www.bristol.ac.uk//Depts//Economics//Growth//barlee.htm.

Outcome : national growth rates in GDP per capita for the periods 1965-1975.
intercept: Constant.
gdpsh465 : Real GDP per capita (1980 international prices) in 1965
bmp1l : Black market premium. Log (1+BMP)
freeop : Measure of "Free trade openness
freetar : Measure of tariff restriction
h65 : Total gross enrollment ratio for higher education in 1965.
hm65 : Male gross enrollment ratio for higher education in 1965.
hf65 : Female gross enrollment ratio for higher education in 1965.
p65 : Total gross enrollment ratio for primary education in 1965.
pm65 : Male gross enrollment ratio for primary education in 1965.
pf65 : Female gross enrollment ratio for primary education in 1965.
s65 : Total gross enrollment ratio for secondary education in 1965.
sm65 : Male gross enrollment ratio for secondary education in 1965.
sf65 : Female gross enrollment ratio for secondary education in 1965.
fert65 : Total fertility rate (children per woman) in 1965.
mort65 : Infant Mortality Rate in 1965.
lifee065 : Life expectancy at age 0 in 1965.
gpop1 : Growth rate of population.
fert1 : Total fertility rate (children per woman).
mort1 : Infant Mortality Rate (ages 0-1).
invsh41 : Ratio of real domestic investment (private plus public) to real GDP.
geetot1 : Ratio of total nominal government expenditure on education to nominal GDP.
geerec1 : Ratio of recurring nominal government expenditure on education to nominal GDP.
gde1 : Ratio of nominal government expenditure on defense to nominal GDP.
govwb1 : Ratio of nominal government "consumption" expenditure to nominal GDP (using current local currency).
govsh41 : Ratio of real government "consumption" expenditure to real GDP. (Period average).
gvxdxe41 : Ratio of real government "consumption" expenditure net of spending on defense and on education to real GDP.
high65 : Percentage of "higher school attained" in the total pop in 1965.
highm65 : Percentage of "higher school attained" in the male pop in 1965.
highf65 : Percentage of "higher school attained" in the female pop in 1965.
highc65 : Percentage of "higher school complete" in the total pop.
highcm65 : Percentage of "higher school complete" in the male pop.
highcf65 : Percentage of "higher school complete" in the female pop.
human65 : Average schooling years in the total population over age 25 in 1965.
humanm65 : Average schooling years in the male population over age 25 in 1965.
humanf65 : Average schooling years in the female population over age 25 in 1965.
hyr65 : Average years of higher schooling in the total population over age 25.
hyrm65 : Average years of higher schooling in the male population over age 25.
hyrf65 : Average years of higher schooling in the female population over age 25.
no65 : Percentage of "no schooling" in the total population.
nom65 : Percentage of "no schooling" in the male population.
nof65 : Percentage of "no schooling" in the female population.
pinstab1 : Measure of political instability.
pop65 : Total Population in 1965.
worker65 : Ratio of total Workers to population.
pop1565 : Population Proportion under 15 in 1965.
pop6565 : Population Proportion over 65 in 1965.
sec65 : Percentage of "secondary school attained" in the total pop in 1965.
secm65 : Percentage of "secondary school attained" in male total pop in 1965.
secf65 : Percentage of "secondary school attained" in female total pop in 1965.
secc65 : Percentage of "secondary school complete" in the total pop in 1965.
seccm65 : Percentage of "secondary school complete" in the total pop in 1965.
seccf65 : Percentage of "secondary school complete" in female pop in 1965.
syr65 : Average years of secondary schooling in the total population over age 25 in 1965.
syrm65 : Average years of secondary schooling in the male population over age 25 in 1965.
syrf65 : Average years of secondary schooling in the female population over age 25 in 1965.
teapri65 : Pupil/Teacher Ratio in primary school.
teasex65 : Pupil/Teacher Ratio in secondary school
ex1 : Ratio of export to GDP (in current international prices)
im1 : Ratio of import to GDP (in current international prices)
xr65 : Exchange rate (domestic currency per U.S. dollar) in 1965.
tot1 : Terms of trade shock (growth rate of export prices minus growth rate of import prices).