# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

# 基本的な考え方
# a全体の最頻値Aがaの要素数の過半数を越えているならば，
# aをどの位置で2分割しても 左の配列と右の配列のどちらか or 両方の配列の最頻値はAである
# → 二分割した祭に両方の配列の配列の最頻値がA以外かつ過半数を満たすことはない
# 左配列はstackで積み上げればOK
# 右配列はstackを消しながらでOK(NULLの場合はAを追加する → 上記の理由化らA以外が最頻値になることは無いはず)

# ↑のアルゴリズムガバ
# rightStackの変更履歴を全て記憶しておいて，毎回読み込んでくればOK

def solution(a)
  # write your code in Ruby 2.2
  n = a.length
  # rightstackの構築とログ保存
  rightStack = []
	rightHash = Hash.new(0)
  rightStackLog = []
  (n - 1).downto(0) do |i|
		rightHash[a[i]] += 1
    if rightStack.length == 0
      ngo = rightHash[a[i]] > (n - i) / 2 ? a[i] : nil     
      rightStack << ngo 
    elsif a[i] == rightStack[-1]
      rightStack << a[i] 
    else
      rightStack.pop 
    end
    rightStackLog << rightStack[-1]
  end

  cnt = 0
  # leftstackの構築とrightstackとの比較
  leftStack = []
  leftHash = Hash.new(0)
  (n-1).times do |i|
    leftHash[a[i]] += 1
    if leftStack.length == 0
      ngo = leftHash[a[i]] > (i + 1) / 2 ? a[i] : nil 
      leftStack << ngo
    elsif a[i] == leftStack[-1]
      leftStack << a[i]
    else 
      leftStack.pop
    end 

    # puts "i:#{i} left:#{leftStack[-1]} log:#{rightStackLog[-2-i]}}"
    # p leftStack
    # p rightStackLog
    # puts     
    cnt += 1 if leftStack[-1] == rightStackLog[-2 - i] && leftStack[-1] != nil
  end
  return cnt 
end
