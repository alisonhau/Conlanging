;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;                                                                     ;;;
;;;                     Carnegie Mellon University                      ;;;
;;;                  and Alan W Black and Kevin Lenzo                   ;;;
;;;                      Copyright (c) 1998-2000                        ;;;
;;;                        All Rights Reserved.                         ;;;
;;;                                                                     ;;;
;;; Permission is hereby granted, free of charge, to use and distribute ;;;
;;; this software and its documentation without restriction, including  ;;;
;;; without limitation the rights to use, copy, modify, merge, publish, ;;;
;;; distribute, sublicense, and/or sell copies of this work, and to     ;;;
;;; permit persons to whom this work is furnished to do so, subject to  ;;;
;;; the following conditions:                                           ;;;
;;;  1. The code must retain the above copyright notice, this list of   ;;;
;;;     conditions and the following disclaimer.                        ;;;
;;;  2. Any modifications must be clearly marked as such.               ;;;
;;;  3. Original authors' names are not deleted.                        ;;;
;;;  4. The authors' names are not used to endorse or promote products  ;;;
;;;     derived from this software without specific prior written       ;;;
;;;     permission.                                                     ;;;
;;;                                                                     ;;;
;;; CARNEGIE MELLON UNIVERSITY AND THE CONTRIBUTORS TO THIS WORK        ;;;
;;; DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING     ;;;
;;; ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT  ;;;
;;; SHALL CARNEGIE MELLON UNIVERSITY NOR THE CONTRIBUTORS BE LIABLE     ;;;
;;; FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES   ;;;
;;; WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN  ;;;
;;; AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,         ;;;
;;; ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF      ;;;
;;; THIS SOFTWARE.                                                      ;;;
;;;                                                                     ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;
;;; Phonset for cmu_awh
;;;

;;;  Feeel free to add new feature values, or new features to this
;;;  list to make it more appropriate to your language

;; This is where it'll fall over if you haven't defined a 
;; a phoneset yet, if you have, delete this, if you haven't
;; define one then delete this error message

(defPhoneSet
  cmu_awh
  ;;;  Phone Features
  (;; vowel or consonant
   (clst + - 0)
   (vc + - 0)
   ;; vowel length: short long dipthong schwa
   (vlng s l d a 0)
   ;; vowel height: high high mid-high mid-high mid-low low
   (vheight 1 2 3 4 5 0 -)
   ;; vowel frontness: front mid back
   (vfront 1 2 3 0 -)
   ;; lip rounding
   (vrnd + - 0)
   ;; consonant type: stop fricative affricative nasal liquid approximant click
   (ctype s f a n l r c 0)
   ;; place of articulation: labial alveolar palatal
   ;; labio-dental dental velar glottal post-alveolar
   (cplace l a p b d v g j 0)
   ;; consonant voicing
   (cvox + - 0)
   (asp  + - 0)
   (nuk + - 0)
   )
  (
   (    pau   -   -   0   0   0   0   0   0   -   -   -   ) 
   (	a - + s 5 1 - 0 0 0 - - )
   (	I - + s 2 1 - 0 0 0 - - )
   (	i - + s 1 1 - 0 0 0 - - )
   (	e - + s 3 1 - 0 0 0 - - )
   (	E - + s 4 1 - 0 0 0 - - )
   (	W - + s 1 3 - 0 0 0 - - )
   (	A - + s 5 3 - 0 0 0 - - )
   (	U - + s 1 3 - 0 0 0 - - )
   (	eI - + d 3 1 - 0 0 0 - - )
   (	N - - 0 0 0 0 n v + - - )
   (	s - - 0 0 0 0 f a - - - )
   (	r - - 0 0 0 0 r a + - - )
   (	z - - 0 0 0 0 f a + - - )
   (	Z - - 0 0 0 0 f j + - - )
   (	x - - 0 0 0 0 f v - - - )
   (	n - - 0 0 0 0 n a + - - )
   (	m - - 0 0 0 0 n l + - - )
   (	H - - 0 0 0 0 f g + - - )
   (	l - - 0 0 0 0 l a + - - )

	;; phonemes here are only the ones necesary for talking clock

  )
)

(PhoneSet.silences '(pau))

(define (cmu_awh_alison::select_phoneset)
  "(cmu_awh_alison::select_phoneset)
Set up phone set for cmu_awh."
  (Parameter.set 'PhoneSet 'cmu_awh)
  (PhoneSet.select 'cmu_awh)
)

(define (cmu_awh_alison::reset_phoneset)
  "(cmu_awh_alison::reset_phoneset)
Reset phone set for cmu_awh."
  t
)

(provide 'cmu_awh_alison_phoneset)
