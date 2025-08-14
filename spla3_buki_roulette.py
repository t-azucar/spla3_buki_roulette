import collections.abc
import streamlit as st
import random as rd
import streamlit.components.v1 as stc

st.title('ブキルーレットアプリ')
st.caption('created by t-azucar')
st.subheader('スプラ3全通常ブキ160種')

l = ['わかば', 
    'もみじ', 
    'ボールド', 
    'ボルネオ',
    'シャーカー',
    'シマネ',
    'シャプゲコ',
    'スシ',
    'スシコラ',
    'スシ煌',
    'プライム',
    'プラコラ',
    'プラフロ',
    '52',
    '52デコ',
    '96',
    '96デコ',
    '96爪',
    'ジェッスイ',
    'ジェッカス',
    'ジェッコブ',
    '黒ザップ',
    '赤ザップ',
    '銀モデ',
    '金モデ',
    '彩モデ',
    'スペシ',
    'スペコラ',
    'L3',
    'L3D',
    'L3箔',
    'H3',
    'H3D',
    'H3スネーク',
    'ボトル',
    'ボイル',
    'ホッブラ',
    'ホッカス',
    '艶ホット',
    'ロンブラ',
    'ロンカス',
    'ラピブラ',
    'ラピデコ',
    'エリブラ',
    'エリデコ',
    'エリ冬',
    'ノヴァ',
    'ノヴァネオ',
    'クラブラ',
    'クラネオ',
    'Sブラ',
    'クイブラ',
    'スプロラ',
    'ロラコラ',
    'カーボン',
    'カーデコ',
    'カーアン',
    'ヴァリアブル',
    'ヴァリフォイ',
    'ダイナモ',
    'テスラ',
    '冥ナモ',
    'ワイロ',
    'ワイコラ',
    'ワイ惑',
    'パブロ',
    'パブヒュー',
    'ホクサイ',
    'ホクヒュー',
    'ホク彗',
    'フィン',
    'フィンヒュー',
    'フィンブロ',
    'スプチャ',
    'チャーコラ',
    'チャーフォレ',
    'スプスコ',
    'スココラ',
    'スコフォレ',
    'リッター',
    'リッカス',
    'リッスコ',
    'スコカス',
    'スクイクa',
    'スクイクb',
    '甲竹',
    '乙竹',
    'ソイチュ',
    'ソイカス',
    '青鉛筆',
    '赤鉛筆',
    'バケスロ',
    'バケデコ',
    'ヒッセン',
    'ヒッヒュー',
    '灰ヒッセン',
    'スクスロ',
    'スクネオ',
    'エクス',
    'エッカス',
    'オフロ',
    'フロデコ',
    'モップ',
    'モップD',
    '角モップ',
    'バレル',
    'バレデコ',
    'スプスピ',
    'スピコラ',
    'スピパイ',
    'ハイドラ',
    'ハイカス',
    'ハイ圧',
    'クーゲル',
    'クゲヒュー',
    'ノーチ',
    '金ノーチ',
    'イグザミ',
    'イグヒュー',
    'スプマニュ',
    'マニュコラ',
    '耀マニュ',
    'ケルビン',
    'ケルデコ',
    'デュアル',
    'デュアカス',
    'デュア蹄',
    '赤スパ',
    '青スパ',
    '黒スパ',
    '黒クア',
    '白クア',
    'ガエン',
    'ガエカス',
    'パラ',
    'パラソレ',
    'キャンプ',
    'キャンソレ',
    'キャンクリ',
    'スパイ',
    'スパソレ',
    'スパ繚',
    '甲傘',
    '乙傘',
    'トラスト',
    'トラコラ',
    'トラ燈',
    'ラクト',
    'ラクデコ',
    'ラクミル',
    'フルイド',
    'フルカス',
    'ドライブ',
    'ドブデコ',
    'ドララス',
    'ジム',
    'ジムヒュー',
    '黒ジム',
    '青デンタル',
    '黒デンタル']

css = r'''
    <style>
        [data-testid="stForm"] {border: 0px}
    </style>
'''
    
st.markdown(css, unsafe_allow_html=True)

with st.form(key='player_info', enter_to_submit=False):
    duplication_category = st.radio('【重複】', ('あり', 'なし'), horizontal=True)
    population_category = st.radio('【人数】', ('1', '2', '3', '4', '5', '6', '7', '8'), horizontal=True)

    st.text('プレイヤー名を入力（※任意）')

    col1, col2 = st.columns(2)

    with col1:
        p1 = st.text_input('', value='', placeholder='player 1', label_visibility='collapsed')
        p2 = st.text_input('', value='', placeholder='player 2', label_visibility='collapsed')
        p3 = st.text_input('', value='', placeholder='player 3', label_visibility='collapsed')
        p4 = st.text_input('', value='', placeholder='player 4', label_visibility='collapsed')
    with col2:
        p5 = st.text_input('', value='', placeholder='player 5', label_visibility='collapsed')
        p6 = st.text_input('', value='', placeholder='player 6', label_visibility='collapsed')
        p7 = st.text_input('', value='', placeholder='player 7', label_visibility='collapsed')
        p8 = st.text_input('', value='', placeholder='player 8', label_visibility='collapsed')

    if duplication_category == 'あり':
        l2 = rd.choices(l, k=8)
    else:
        l2 = rd.sample(l, 8)

    if p1 == '':
        p1 = '1'
    if p2 == '':
        p2 = '2'
    if p3 == '':
        p3 = '3'
    if p4 == '':
        p4 = '4'
    if p5 == '':
        p5 = '5'
    if p6 == '':
        p6 = '6'
    if p7 == '':
        p7 = '7'
    if p8 == '':
        p8 = '8'
        
    if population_category == '1':
        order =  l2[0]
    elif population_category == '2':
        order = p1 + '＝' + l2[0] + ' | ' + p2 + '＝' + l2[1]
    elif population_category == '3':
        order = p1 + '＝' + l2[0] + ' | ' + p2 + '＝' + l2[1] + ' | ' + p3 + '＝' + l2[2]
    elif population_category == '4':
        order = p1 + '＝' + l2[0] + ' | ' + p2 + '＝' + l2[1] + ' | ' + p3 + '＝' + l2[2] + ' | ' + p4 + '＝' + l2[3]
    elif population_category == '5':
        order = p1 + '＝' + l2[0] + ' | ' + p2 + '＝' + l2[1] + ' | ' + p3 + '＝' + l2[2] + ' | ' + p4 + '＝' + l2[3] + \
        ' | ' + p5 + '＝' + l2[4]
    elif population_category == '6':
        order = p1 + '＝' + l2[0] + ' | ' + p2 + '＝' + l2[1] + ' | ' + p3 + '＝' + l2[2] + ' | ' + p4 + '＝' + l2[3] + \
        ' | ' + p5 + '＝' + l2[4] + ' | ' + p6 + '＝' + l2[5]
    elif population_category == '7':
        order = p1 + '＝' + l2[0] + ' | ' + p2 + '＝' + l2[1] + ' | ' + p3 + '＝' + l2[2] + ' | ' + p4 + '＝' + l2[3] + \
        ' | ' + p5 + '＝' + l2[4] + ' | ' + p6 + '＝' + l2[5] + ' | ' + p7 + '＝' + l2[6]
    else:
        order = p1 + '＝' + l2[0] + ' | ' + p2 + '＝' + l2[1] + ' | ' + p3 + '＝' + l2[2] + ' | ' + p4 + '＝' + l2[3] + \
        ' | ' + p5 + '＝' + l2[4] + ' | ' + p6 + '＝' + l2[5] + ' | ' + p7 + '＝' + l2[6] + ' | ' + p8 + '＝' + l2[7]

    html_content = f"""
    <button onclick="navigator.clipboard.writeText('{order}')">
        コピー
    </button>
    """

    submit_btn = st.form_submit_button('ルーレット実行', type='primary')
    if submit_btn:
        st.code(order, language=None, wrap_lines=True)
        stc.html(html_content, height=50)
