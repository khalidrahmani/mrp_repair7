# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

#-------------------------------------------------------------
# French
#-------------------------------------------------------------


to_19_fr = ( 'Zéro',  'Un',   'Deux',  'Trois', 'Quatre',   'Cinq',   'Six',
          'Sept', 'Huit', 'Neuf', 'Dix', 'Onze', 'Douze', 'Treize',
          'Quatorze', 'Quinze', 'Seize', 'Dix-sept', 'Dix-huit', 'Dix-neuf' )
tens_fr  = ( 'Vingt', 'Trente', 'Quarante', 'Cinquante', 'Soixante', 'Soixante-dix', 'Quatre-vingts', 'Quatre-vingt Dix')
denom_fr = ( '',
          'Mille',     'Million',         'Milliard',       'Billion',       'Quadrillion',
          'Quintillion',  'Sextillion',      'Septillion',    'Octillion',      'Nonillion',
          'Décillion',    'Undecillion',     'Duodecillion',  'Tredecillion',   'Quattuordecillion',
          'Sexdecillion', 'Septendecillion', 'Octodecillion', 'Icosillion', 'Vigintillion' )

def _convert_nn_fr(val):
    """ convert a value < 100 to French
    """
    if val < 20:
        return to_19_fr[val]
    for (dcap, dval) in ((k, 20 + (10 * v)) for (v, k) in enumerate(tens_fr)):
        if dval + 10 > val:
            if val % 10:
                return dcap + '-' + to_19_fr[val % 10]
            return dcap

def _convert_nnn_fr(val):
    """ convert a value < 1000 to french
    
        special cased because it is the level that kicks 
        off the < 100 special case.  The rest are more general.  This also allows you to
        get strings in the form of 'forty-five hundred' if called directly.
    """
    word = ''
    (mod, rem) = (val % 100, val // 100)
    if rem == 1:
        word = ' Cent'
        if mod > 0:
            word = word + ' '
    if rem > 1:
        word = to_19_fr[rem] + ' Cent'
        if mod > 0:
            word = word + ' '
    if mod > 0:
        word = word + _convert_nn_fr(mod)
    return word

def french_number(val):
    if val < 100:
        return _convert_nn_fr(val)
    if val < 1000:
         return _convert_nnn_fr(val)
    for (didx, dval) in ((v - 1, 1000 ** v) for v in range(len(denom_fr))):
        if dval > val:
            mod = 1000 ** didx
            l = val // mod
            r = val - (l * mod)
            if l == 1:
                if didx > 1:
                    ret = _convert_nnn_fr(l) + ' ' + denom_fr[didx]
                else :
                    ret = ' ' + denom_fr[didx]  
            elif l > 1:
                ret = _convert_nnn_fr(l) + ' ' + denom_fr[didx]+'s'
            if r > 0:
                ret = ret + ', ' + french_number(r)
            return ret

def amount_to_text_fr(number, currency):
    number = '%.2f' % number
    units_name = currency
    list = str(number).split('.')
    start_word = french_number(abs(int(list[0])))
    end_word = french_number(int(list[1]))
    cents_number = int(list[1])
    cents_name = (cents_number > 1) and ' Centimes' or ' Centime'
    final_result = start_word +' '+units_name+' '+ end_word +' '+cents_name
    return final_result

def amount_to_text(nbr, lang='fr', currency='euro'):
    return amount_to_text_fr(abs(nbr), currency)

if __name__=='__main__':
    from sys import argv
    
    lang = 'fr'
    if len(argv) < 2:
        for i in range(1,200):
            print i, ">>", amount_to_text(i, lang)
        for i in range(200,999999,139):
            print i, ">>", amount_to_text(i, lang)
    else:
        print amount_to_text(int(argv[1]), lang)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

