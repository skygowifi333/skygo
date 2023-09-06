import streamlit as st
import pandas as pd
import datetime


# ページのタイトル（なくてもいい）
st.title('Skygo')

# ファイルアップローダーの準備
uploaded_file = st.file_uploader("Upload xlsx", type="xlsx")

# uploadファイルが存在するときだけ、csvファイルの読み込みがされる。
if uploaded_file is not None:
    dataframe = pd.read_excl(uploaded_file)
    
    #国を選ぶセレクトボックス追加   
    selected_country = st.selectbox("Choose Country", ["ALL","USA", "JAPAN"])

    #国別に分類
    dataframe_us = dataframe.query("`Continent name` == 'USA'")
    dataframe_jp = dataframe.query("`Continent name` == 'Japan'") 
    dataframe_all = dataframe

    # 選択された国に応じてデータフレームをフィルタリング
    if selected_country == "USA":
        dataframe_filtered = dataframe_us
    elif selected_country == "JAPAN":
        dataframe_filtered = dataframe_jp
    else:
        dataframe_filtered = dataframe_all

    # 利用開始日と利用終了日が含まれる列名
    start_date_column = 'From date'
    end_date_column = 'To date'

    #現在の日付
    date = datetime.date.today()

    #範囲の初期設定
    date_start= date + datetime.timedelta(weeks=-53)
    date_end= date + datetime.timedelta(weeks=53)

    # 日付データを日付型に変換
    dataframe_filtered[start_date_column] = pd.to_datetime(dataframe_filtered[start_date_column])
    dataframe_filtered[end_date_column] = pd.to_datetime(dataframe_filtered[end_date_column])
    
    # 利用したい期間を指定-1年
    start_date = pd.Timestamp(date_start)
    #今日の日付+1年まで
    end_date = pd.Timestamp(date_end)

    # 指定した期間内のデータを抽出
    selected_data = dataframe_filtered[
        (dataframe_filtered[start_date_column] >= start_date) &
        (dataframe_filtered[end_date_column] <= end_date)
    ]

    # 各日ごとにデータ数をカウント
    daily_counts = pd.date_range(start_date, end_date, freq='D').to_series().apply(
        lambda day: selected_data[
            (day >= selected_data[start_date_column]) &
            (day <= selected_data[end_date_column])
        ].shape[0]
    )

    # 表として書き出される
    with st.expander("See  All Data"):
        st.write(dataframe)
        st.line_chart(daily_counts)

    #One Day検索
    with st.expander("One Day"):
        d = st.date_input('Input Day', date, min_value=date_start, max_value=date_end)
        date_input=d.strftime('%m/%d/%Y')
        if date_input:
           
            # 各日ごとにデータ数をカウント
            daily_counts = pd.date_range(start_date, end_date, freq='D').to_series().apply(
                lambda day: selected_data[
                    (day >= selected_data[start_date_column]) &
                    (day <= selected_data[end_date_column])
                ].shape[0]
            )
            # 結果を表示
            daily_counts = daily_counts.to_frame()
            st.write(daily_counts.loc[date_input])

    #初期設定
    date_start_More= date + datetime.timedelta(weeks=-1)
    date_end_More= date + datetime.timedelta(weeks=1)

    with st.expander("More Day"):
        # データの入力
        date_start_More = st.date_input('Input Strat Date', date_start_More, min_value=date_start, max_value=date_end)
        date_end_More = st.date_input('Input End Date', date_end_More, min_value=date_start, max_value=date_end)

        # 選択した日付範囲をdatetime型に変換
        date_start_More = datetime.datetime.combine(date_start_More, datetime.time())
        date_end_More = datetime.datetime.combine(date_end_More, datetime.time())

        # データ型の変換
        date_start_More_str = date_start_More.strftime('%m/%d/%Y')
        date_end_More_str = date_end_More.strftime('%m/%d/%Y')

        More_data = daily_counts.loc[date_start_More_str:date_end_More_str]

        # データの表示
        st.dataframe(More_data)
        st.line_chart(More_data)

       
       
