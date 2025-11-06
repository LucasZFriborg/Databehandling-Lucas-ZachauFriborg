# Pandas – syntax

### läsa in data
`df = pd.read_csv('fil.csv', sep=';')`
sep=';' behövs ofta i Europa.
Detta läser in CSV till en tabell i pandas.
`df = pd.read_csv('data.csv', index_col=0)`
`index_col` = vilken kolumn som ska bli index när man läser in en fil.

### titta på kolumner
`df.columns`
Visar namnen på alla kolumner i datan.

### välja kolumn
`df['age']`
Hämtar en kolumn.

### välja flera kolumner
`df[['age','health']]`
Hämtar två eller fler kolumner.

### filter – välja rader
`df[df['age'] > 20]`
Visar bara rader där age > 20 är sant.

### drop – ta bort kolumn eller rader
`df = df.drop(columns=['age'])`
Tar bort specifik kolumn.

### rename – byta namn på kolumn
`df = df.rename(columns={'age':'Years'})`
Byter kolumnnamn (t.ex för att göra datan tydligare).

### rename flera kolumner
`df.columns = ['col1','col2','col3']`
Sätter alla kolumnnamn på en gång.

### insert – lägga till kolumn på specifik plats
`df.insert(0, 'newcol', 1)`
Lägger ny kolumn på position 0 (första column).

### reset_index – gör index till kolumn igen
`df = df.reset_index()`
Används mycket efter filtrering / groupby.

### loc – välj med etiketter (labels)
`df.loc[0,'age']`
Välj rad 0 och kolumn 'age'.

### iloc – välj med indexnummer
`df.iloc[0,2]`
Samma som loc men indexnummer istället för namn.

### isna – hitta saknade värden
`df.isna().sum()`
Samma som isnull(), bara modernare syntax.

### isnull – vilka celler är NaN?
`df.isnull()`
ger True/False för varje cell som saknar värde.

### isnull + sum – räkna antal NaN per kolumn
`df.isnull().sum()`
räknar hur många NaN varje kolumn har.

### notnull – motsats till isnull
`df.notnull()`
True för celler som INTE är tomma.

### filtrera rader där en kolumn är NaN
`df[df['age'].isnull()]`
ger alla rader där age saknas.
`rows_age = df[df['age'].isnull()]`
print(f'Rows where age is NaN: \n`{rows_age.index}`')
.index visar vilka radnummer som saknar värde i age.

### filtrera rader där kolumn inte är NaN
`df[df['age'].notnull()]`
alla rader där age finns.

### OR-villkor (|) – minst ett villkor sant
`df[df['age'].isnull() | df['freetime'].isnull()]`
rader där age eller freetime saknar värde.

### AND-villkor (&) – båda villkor måste vara sanna
`df[(df['age'] > 15) & (df['age'] < 18)]`
rader där age är mellan 16–17.
man måste wrap:a villkoren i ( )

### notna – hitta värden som inte är NaN
`df[df['age'].notna()]`
Filtrera bort tomma celler.

### dtypes – se datatyper
`df.dtypes`
Visar typ per kolumn (int, float, object etc).

### str-functions – text i kolumner
`df['name'].str.upper()`
Använd str för textbehandling (uppercase, replace etc).

### save to csv
`df.to_csv('fil.csv', index=False)`
Spara DataFrame till csv.

### read excel
`df = pd.read_excel('fil.xlsx')`
Läs excel-fil.

### write excel
`df.to_excel('fil.xlsx', index=False)`
Spara DataFrame till excel.

### read
`df.head()`
Visar de första raderna – snabbt för att se vad det är för data.

### describe
`df.describe()`
Snabb statistik för numeriska kolumner (mean, std, min, max, etc)

### info
`df.info()`
Visar datatyper och om kolumner innehåller NaN.

### shape
`df.shape`
Ger (antal_rader, antal_kolumner)

### unique
`df['sex'].unique()`
Visar unika värden i en kolumn (kategori-värden).

### value_counts
`df['school'].value_counts()`
Räknar hur många av varje kategori som finns.

### mean / median / std – basic statistik
`df['age'].mean()`
`df['age'].median()`
`df['age'].std()`
Ger medelvärde, median och standardavvikelse.

### groupby
`df.groupby('school')['absences'].mean()`
Delar upp i grupper och räknar statistik per grupp.

### pivot_table
`df.pivot_table(index='school', columns='sex', values='age', aggfunc='mean')`
Tvådimensionell tabell – statistik per två kategorier.

### sorting
`df.sort_values('age', ascending=False)`
Sorterar data (t.ex från högsta till lägsta ålder).

### pandas plot
`df['age'].plot(kind='hist')`
`plt.show()`
Gör diagram direkt från pandas.

### seaborn plot
`sns.boxplot(data=df, x='sex', y='age')`
`plt.show()`
Seaborn = lättare och snyggare visualiseringar.

### Plotly Express
`import plotly.express as px`
`fig = px.line(df, x='datum', y='värde')`
`fig.show()`.
Exempel på användning:
`px.scatter(df, x='längd', y='vikt')`
`px.bar(df, x='kategori', y='antal')`
`px.histogram(df, x='ålder')`
`px.box(df, y='inkomst')`
`px.area(df, x='tid', y='försäljning')`.
Plotly Express är en modul i Plotly som gör det enkelt att: visualisera data, 
klicka/zooma i grafen, se hover-värden (t.ex. “det här punktens exakta värde”)

### apply
`df['double_age'] = df['age'].apply(lambda x: x*2)`
Skapar ny kolumn genom att köra funktion på varje värde.

### value_counts (kategoridata)
`df['school'].value_counts()`
Räknar hur många per kategori (samma som 11).

### merge (SQL JOIN)
`pd.merge(df1, df2, on='id', how='left')`
Slår ihop två tabeller via gemensam kolumn – som i SQL.
`pd.merge(left, right, on='key', indicator=True)`
`indicator=True` gör att pandas lägger till en extra kolumn i resultatet som visar varje rad kom ifrån.
Kolumnen heter: '_merge'
left_only - raden fanns bara i left
right_only - raden fanns bara i right
both - raden fanns i båda
Man använder indicator=True när man vill kolla vilka rader som matchade i merget och vilka som saknas.

### concat
`pd.concat([df1, df2], axis=0)` eller `pd.concat([df1, df2], axis='index')`
Lägger ihop två tabeller ovanpå varandra, staplar rader (vertikalt).
`pd.concat([df1, df2], axis=1)` eller `pd.concat([df1, df2], axis='columns')`
Lägger ihop två tabeller bredvid varandra, staplar kolumner (horisontalt).

### join= i concat
`pd.concat([df1, df2], axis=1, join='outer')`
`pd.concat([df1, df2], axis=1, join='inner')`
`join='outer'` (default) - behåll alla index från båda dfs → saknade värden blir NaN
`join='inner` - behåll bara index som finns i båda dfs → allt annat slängs

### melt (wide till long)
`pd.melt(df, id_vars=['student'], value_vars=['math','english'])`
Gör om flera kolumner till rader.

### pivot (long till wide)
`df.pivot(index='student', columns='subject', values='score')`
Gör om rader till kolumner.

### dropna
`df = df.dropna(subset=['age'])`
Tar bort rader som saknar värde i en viss kolumn.

### fillna
`df['age'] = df['age'].fillna(df['age'].mean())`
Fyller in saknade värden t.ex med medelvärde.

### replace
`df['health'] = df['health'].replace({1:'bad', 5:'great'})`
Byter ut vissa värden mot nya.

### astype
`df['age'] = df['age'].astype(int)`
Byter datatyp (t.ex float till int).

### pd.to_datetime
`df['date'] = pd.to_datetime(df['date'])`
Gör om text till datum.

### set_index (datetime)
`df = df.set_index('date')`
Sätter datum som index → viktigt för tidsserier.

### resample
`df.resample('M').mean()`
Gör om tidsdata till perioder (t.ex per månad) och beräknar statistik per period.

### rolling window
`df['7day_avg'] = df['value'].rolling(7).mean()`
Rullande medelvärde – bra för grafer över tid.