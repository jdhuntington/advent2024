#!/usr/bin/env ruby

answer = 0
ARGF.each do |l|
  terms = l.strip.split.map(&:to_i)
  terms.permutation(terms.length - 1).each do |x|
    ascending = x.sort
    descending = ascending.reverse
    next unless ascending == x || descending == x
    ok = true
    x.each_with_index do |y, i|
      break if i == x.length - 1
      ok = false unless (1 <= (y - x[i+1]).abs) && ((y - x[i+1]).abs <= 3)
    end
    next unless ok
    answer += 1
    puts "(#{x.join(', ')})"
    break
  end
end
puts answer
