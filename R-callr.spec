#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-callr
Version  : 3.7.0
Release  : 59
URL      : https://cran.r-project.org/src/contrib/callr_3.7.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/callr_3.7.0.tar.gz
Summary  : Call R from R
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-processx
BuildRequires : R-R6
BuildRequires : R-processx
BuildRequires : buildreq-R

%description
separate R process, without affecting the current R process at all.
    This packages does exactly that.

%prep
%setup -q -c -n callr
cd %{_builddir}/callr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619024408

%install
export SOURCE_DATE_EPOCH=1619024408
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library callr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library callr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library callr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc callr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/callr/DESCRIPTION
/usr/lib64/R/library/callr/INDEX
/usr/lib64/R/library/callr/LICENSE
/usr/lib64/R/library/callr/Meta/Rd.rds
/usr/lib64/R/library/callr/Meta/features.rds
/usr/lib64/R/library/callr/Meta/hsearch.rds
/usr/lib64/R/library/callr/Meta/links.rds
/usr/lib64/R/library/callr/Meta/nsInfo.rds
/usr/lib64/R/library/callr/Meta/package.rds
/usr/lib64/R/library/callr/NAMESPACE
/usr/lib64/R/library/callr/NEWS.md
/usr/lib64/R/library/callr/R/callr
/usr/lib64/R/library/callr/R/callr.rdb
/usr/lib64/R/library/callr/R/callr.rdx
/usr/lib64/R/library/callr/WORDLIST
/usr/lib64/R/library/callr/developer-notes.md
/usr/lib64/R/library/callr/help/AnIndex
/usr/lib64/R/library/callr/help/aliases.rds
/usr/lib64/R/library/callr/help/callr.rdb
/usr/lib64/R/library/callr/help/callr.rdx
/usr/lib64/R/library/callr/help/paths.rds
/usr/lib64/R/library/callr/html/00Index.html
/usr/lib64/R/library/callr/html/R.css
/usr/lib64/R/library/callr/tests/testthat.R
/usr/lib64/R/library/callr/tests/testthat/fixtures/D1
/usr/lib64/R/library/callr/tests/testthat/fixtures/csomag/DESCRIPTION
/usr/lib64/R/library/callr/tests/testthat/fixtures/csomag/NAMESPACE
/usr/lib64/R/library/callr/tests/testthat/fixtures/csomag/R/libpath.R
/usr/lib64/R/library/callr/tests/testthat/fixtures/script.R
/usr/lib64/R/library/callr/tests/testthat/fixtures/script2.R
/usr/lib64/R/library/callr/tests/testthat/fixtures/simple.txt
/usr/lib64/R/library/callr/tests/testthat/helper.R
/usr/lib64/R/library/callr/tests/testthat/test-archs.R
/usr/lib64/R/library/callr/tests/testthat/test-bugs.R
/usr/lib64/R/library/callr/tests/testthat/test-callback.R
/usr/lib64/R/library/callr/tests/testthat/test-clean-subprocess.R
/usr/lib64/R/library/callr/tests/testthat/test-error.R
/usr/lib64/R/library/callr/tests/testthat/test-eval.R
/usr/lib64/R/library/callr/tests/testthat/test-function-env.R
/usr/lib64/R/library/callr/tests/testthat/test-libpath.R
/usr/lib64/R/library/callr/tests/testthat/test-messages.R
/usr/lib64/R/library/callr/tests/testthat/test-options.R
/usr/lib64/R/library/callr/tests/testthat/test-presets.R
/usr/lib64/R/library/callr/tests/testthat/test-quit.R
/usr/lib64/R/library/callr/tests/testthat/test-r-bg.R
/usr/lib64/R/library/callr/tests/testthat/test-r-process.R
/usr/lib64/R/library/callr/tests/testthat/test-r-session-messages.R
/usr/lib64/R/library/callr/tests/testthat/test-r-session.R
/usr/lib64/R/library/callr/tests/testthat/test-rcmd-bg.R
/usr/lib64/R/library/callr/tests/testthat/test-rcmd-process.R
/usr/lib64/R/library/callr/tests/testthat/test-rcmd.R
/usr/lib64/R/library/callr/tests/testthat/test-rscript.R
/usr/lib64/R/library/callr/tests/testthat/test-spelling.R
/usr/lib64/R/library/callr/tests/testthat/test-timeout.R
/usr/lib64/R/library/callr/tests/testthat/test-utils.R
