# Iris Classification using Machine Learning Algorithms

## Introduction
The [Iris Dataset](https://www.kaggle.com/uciml/iris#) is one of the most common datasets used for beginning with Machine Learning. In the jupyter notebook, I have used this dataset as a brief refresher for data analysis, data visualization, data preparation, model comparisons and finally, training a Machine Learning model. 

<br>

## About The Dataset
The Iris flower data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. 

The data set consists of 50 samples from each of three species of Iris (Iris Setosa, Iris virginica, and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.

<br>

## Python Packages Used

#### Required
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn

#### Optional
- subprocess
- kaggle

<br>

## Model Comparison

<table border="\&quot;1\&quot;" class="\&quot;dataframe\&quot;">

<thead>

<tr style="\&quot;text-align:" right;\"="">

<th></th>

<th>model</th>

<th>fit_time</th>

<th>score_time</th>

<th>test_accuracy</th>

<th>test_precision_weighted</th>

<th>test_recall_weighted</th>

<th>test_f1_weighted</th>

</tr>

</thead>

<tbody>

<tr>

<th>0</th>

<td>LogReg</td>

<td>0.033801</td>

<td>0.002941</td>

<td>0.958333</td>

<td>0.965278</td>

<td>0.958333</td>

<td>0.959235</td>

</tr>

<tr>

<th>1</th>

<td>LogReg</td>

<td>0.028501</td>

<td>0.002927</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

</tr>

<tr>

<th>2</th>

<td>LogReg</td>

<td>0.021409</td>

<td>0.002904</td>

<td>0.916667</td>

<td>0.944444</td>

<td>0.916667</td>

<td>0.919048</td>

</tr>

<tr>

<th>3</th>

<td>LogReg</td>

<td>0.022165</td>

<td>0.002827</td>

<td>0.875000</td>

<td>0.877381</td>

<td>0.875000</td>

<td>0.874123</td>

</tr>

<tr>

<th>4</th>

<td>LogReg</td>

<td>0.025666</td>

<td>0.002911</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

</tr>

<tr>

<th>5</th>

<td>RForest</td>

<td>0.140764</td>

<td>0.010662</td>

<td>0.916667</td>

<td>0.940476</td>

<td>0.916667</td>

<td>0.919444</td>

</tr>

<tr>

<th>6</th>

<td>RForest</td>

<td>0.135106</td>

<td>0.010629</td>

<td>0.958333</td>

<td>0.962963</td>

<td>0.958333</td>

<td>0.958462</td>

</tr>

<tr>

<th>7</th>

<td>RForest</td>

<td>0.148307</td>

<td>0.010626</td>

<td>0.916667</td>

<td>0.944444</td>

<td>0.916667</td>

<td>0.919048</td>

</tr>

<tr>

<th>8</th>

<td>RForest</td>

<td>0.150510</td>

<td>0.011301</td>

<td>0.833333</td>

<td>0.833333</td>

<td>0.833333</td>

<td>0.833333</td>

</tr>

<tr>

<th>9</th>

<td>RForest</td>

<td>0.139584</td>

<td>0.011256</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

</tr>

<tr>

<th>10</th>

<td>KNN</td>

<td>0.001731</td>

<td>0.005802</td>

<td>0.916667</td>

<td>0.940476</td>

<td>0.916667</td>

<td>0.919444</td>

</tr>

<tr>

<th>11</th>

<td>KNN</td>

<td>0.001551</td>

<td>0.004280</td>

<td>0.958333</td>

<td>0.962963</td>

<td>0.958333</td>

<td>0.958462</td>

</tr>

<tr>

<th>12</th>

<td>KNN</td>

<td>0.001479</td>

<td>0.004094</td>

<td>0.958333</td>

<td>0.966667</td>

<td>0.958333</td>

<td>0.959259</td>

</tr>

<tr>

<th>13</th>

<td>KNN</td>

<td>0.001776</td>

<td>0.004657</td>

<td>0.916667</td>

<td>0.916667</td>

<td>0.916667</td>

<td>0.916667</td>

</tr>

<tr>

<th>14</th>

<td>KNN</td>

<td>0.001454</td>

<td>0.004048</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

</tr>

<tr>

<th>15</th>

<td>SVM</td>

<td>0.001683</td>

<td>0.002758</td>

<td>0.916667</td>

<td>0.940476</td>

<td>0.916667</td>

<td>0.919444</td>

</tr>

<tr>

<th>16</th>

<td>SVM</td>

<td>0.001634</td>

<td>0.002746</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

</tr>

<tr>

<th>17</th>

<td>SVM</td>

<td>0.001640</td>

<td>0.002713</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

</tr>

<tr>

<th>18</th>

<td>SVM</td>

<td>0.001588</td>

<td>0.003277</td>

<td>0.875000</td>

<td>0.877381</td>

<td>0.875000</td>

<td>0.874123</td>

</tr>

<tr>

<th>19</th>

<td>SVM</td>

<td>0.001606</td>

<td>0.002726</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

</tr>

<tr>

<th>20</th>

<td>GaussNB</td>

<td>0.001543</td>

<td>0.002686</td>

<td>0.958333</td>

<td>0.965278</td>

<td>0.958333</td>

<td>0.959235</td>

</tr>

<tr>

<th>21</th>

<td>GaussNB</td>

<td>0.001510</td>

<td>0.002717</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

</tr>

<tr>

<th>22</th>

<td>GaussNB</td>

<td>0.002260</td>

<td>0.003761</td>

<td>0.916667</td>

<td>0.944444</td>

<td>0.916667</td>

<td>0.919048</td>

</tr>

<tr>

<th>23</th>

<td>GaussNB</td>

<td>0.002753</td>

<td>0.004119</td>

<td>0.833333</td>

<td>0.842172</td>

<td>0.833333</td>

<td>0.829762</td>

</tr>

<tr>

<th>24</th>

<td>GaussNB</td>

<td>0.001635</td>

<td>0.002837</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

</tr>

<tr>

<th>25</th>

<td>XGB</td>

<td>0.020684</td>

<td>0.003223</td>

<td>0.916667</td>

<td>0.940476</td>

<td>0.916667</td>

<td>0.919444</td>

</tr>

<tr>

<th>26</th>

<td>XGB</td>

<td>0.020511</td>

<td>0.003347</td>

<td>0.958333</td>

<td>0.962963</td>

<td>0.958333</td>

<td>0.958462</td>

</tr>

<tr>

<th>27</th>

<td>XGB</td>

<td>0.020172</td>

<td>0.003201</td>

<td>0.916667</td>

<td>0.944444</td>

<td>0.916667</td>

<td>0.919048</td>

</tr>

<tr>

<th>28</th>

<td>XGB</td>

<td>0.023655</td>

<td>0.003335</td>

<td>0.875000</td>

<td>0.877381</td>

<td>0.875000</td>

<td>0.874123</td>

</tr>

<tr>

<th>29</th>

<td>XGB</td>

<td>0.021089</td>

<td>0.003258</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

<td>1.000000</td>

</tr>

</tbody>

</table>

</div>


