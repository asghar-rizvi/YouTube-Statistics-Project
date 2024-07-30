from matplotlib import pyplot as plt
import seaborn as sns

def barPlot(data):
    refine_data = data.groupby(['Abbreviation', 'channel_type']).agg({"uploads": "sum"}).reset_index()

    plt.figure(figsize=(16, 10))

    sns.barplot(data=refine_data,x='Abbreviation',y='uploads',hue='channel_type',edgecolor='black',width=5)

    plt.xticks(rotation=45, ha='right')  # Rotate labels for better readability

    # Add labels and title
    plt.xlabel("Country", fontsize=15)
    plt.ylabel("Total Uploads", fontsize=15)
    plt.title("Uploads According to Country", fontsize=18)

    # Add a legend
    plt.legend(title='Channel Type')

    # Improve layout and display the plot
    plt.tight_layout()
    plt.show()


def scatterPlot(data):
    plt.figure(figsize=(14, 8))
    sns.scatterplot(data=data, x='Abbreviation', y='rank', hue='channel_type', palette="Set2", s=100, alpha=0.7)
    plt.xticks(rotation=45, ha='right')  # Rotate x labels for better readability
    plt.xlabel("Country", fontsize=15)
    plt.ylabel("Rank", fontsize=15)
    plt.title("Scatter Plot of YouTuber Ranks by Country", fontsize=18)
    plt.legend(title='Channel Type')
    plt.show()

def countPlot(data):
    plt.figure(figsize=(14, 8))
    sns.countplot(data=data, x='Abbreviation',width=0.9,color='r')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Country", fontsize=15)
    plt.ylabel("Rank", fontsize=15)
    plt.title("Count Plot Of No.of Channels in Ranking", fontsize=18)
    plt.legend(title='Channel Type')
    plt.show()

def barPlot_Category_views(data):
    refine_data = data.groupby(['Abbreviation', 'channel_type']).agg({"video views": "sum"}).reset_index()
    plt.figure(figsize=(16, 10))

    sns.barplot(data=refine_data, x='Abbreviation', y='video views', hue='channel_type', edgecolor='black', width=5)

    plt.xticks(rotation=45, ha='right')  # Rotate labels for better readability

    # Add labels and title
    plt.xlabel("Country", fontsize=15)
    plt.ylabel("Total Uploads", fontsize=15)
    plt.title("Uploads According to Country", fontsize=18)

    # Add a legend
    plt.legend(title='Channel Type')

    # Improve layout and display the plot
    plt.tight_layout()
    plt.show()

def plot_scatter_with_regression(data):
    plt.figure(figsize=(14, 8))
    sns.regplot(data=data, x='created_year', y='rank', scatter_kws={'s':50, 'alpha':0.7}, line_kws={'color':'red'})
    plt.xlabel("Created Year", fontsize=15)
    plt.ylabel("Rank", fontsize=15)
    plt.title("Scatter Plot of Channel Rank vs Created Year", fontsize=18)
    plt.show()