# -*- encoding: utf-8 -*-
##############################################################################
#
#    check_voucher.py
#    account_voucher_check
#    First author: Mag Guevara <mag.guevara@clearcorp.co.cr> (ClearCorp S.A.)
#    Copyright (c) 2010-TODAY ClearCorp S.A. (http://clearcorp.co.cr). All rights reserved.
#    
#    Redistribution and use in source and binary forms, with or without modification, are
#    permitted provided that the following conditions are met:
#    
#       1. Redistributions of source code must retain the above copyright notice, this list of
#          conditions and the following disclaimer.
#    
#       2. Redistributions in binary form must reproduce the above copyright notice, this list
#          of conditions and the following disclaimer in the documentation and/or other materials
#          provided with the distribution.
#    
#    THIS SOFTWARE IS PROVIDED BY <COPYRIGHT HOLDER> ``AS IS'' AND ANY EXPRESS OR IMPLIED
#    WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
#    FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR
#    CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#    CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#    ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#    NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
#    ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#    
#    The views and conclusions contained in the software and documentation are those of the
#    authors and should not be interpreted as representing official policies, either expressed
#    or implied, of ClearCorp S.A..
#    
##############################################################################

import time
import pooler
from report import report_sxw
from amount_to_text import number_to_text_es
import locale
from tools import debug

class check_voucher(report_sxw.rml_parse):

	def __init__(self, cr, uid, name, context):
		super(check_voucher, self).__init__(cr, uid, name, context=context)
		self.localcontext.update({
			'time': time,
			'cr'  : cr,
			'uid' : uid,
			'get_text':self.get_text,
		})
		self.context = context
		self._node = None

	def get_text(self,amount,currency,lang):
		debug(amount)
		debug(lang)
		separator = ','
		if lang:
			lang_pool = self.pool.get('res.lang')
			id_lang = lang_pool.search(self.cr,self.uid,[('code','=',lang)])
			obj_lang = lang_pool.browse(self.cr,self.uid,[id_lang])
			separator = obj_lang  and obj_lang.thousands_sep or separator
		debug(separator)
		res = number_to_text_es(amount,currency.currency_name,separator)
		return res
		
report_sxw.report_sxw(
    'report.check.voucher.layout_ccorp',
    'account.voucher',
    'addons/account_voucher_check/report/check_voucher.mako',
    parser=check_voucher
)
