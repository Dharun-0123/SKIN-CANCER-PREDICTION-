# 🧪 Testing Guide - SkinCare AI

## Quick Test (2 minutes)

### 1. Start the Server
```bash
cd webapp
python manage.py runserver
```

### 2. Test Basic Functionality
1. Visit: http://127.0.0.1:8000/
2. Click "Register" and create an account
3. Login with your credentials
4. Upload a test image
5. View your analysis history

## Comprehensive Testing

### Performance Testing

#### Run Performance Check
```bash
cd webapp
python scripts/performance_check.py
```

**Expected**: Score 70+

#### Lighthouse Test
1. Open Chrome DevTools (F12)
2. Go to Lighthouse tab
3. Select "Performance" + "Accessibility"
4. Run audit
5. **Expected**: 95+ performance score

### Responsive Testing

#### Method 1: Browser DevTools
1. Visit: http://127.0.0.1:8000/
2. Press **F12** (open DevTools)
3. Press **Ctrl+Shift+M** (toggle device toolbar)
4. Test these sizes:
   - **375px** (iPhone SE)
   - **390px** (iPhone 12)
   - **768px** (iPad)
   - **1024px** (iPad Pro)
   - **1920px** (Desktop)

#### Method 2: Resize Browser
1. Visit: http://127.0.0.1:8000/
2. Resize browser window
3. Check:
   - ✅ No horizontal scroll
   - ✅ Text readable
   - ✅ Buttons clickable
   - ✅ Images scale

### Functionality Testing

#### Authentication
- [ ] Can register new account
- [ ] Can login with credentials
- [ ] Can logout
- [ ] Session persists across pages
- [ ] Protected pages require login

#### Image Upload
- [ ] Can select image file
- [ ] Can drag and drop image
- [ ] Preview shows before upload
- [ ] Upload button activates
- [ ] Analysis completes successfully

#### Results Display
- [ ] Classification shows correctly
- [ ] Medical information displays
- [ ] Prevention tips visible
- [ ] Precautions shown
- [ ] Images display properly

#### History
- [ ] User's analyses show
- [ ] Images display correctly
- [ ] Classifications visible
- [ ] Badges show correctly
- [ ] Stats display properly

### Page Testing

Test each page for:
- ✅ Loads without errors
- ✅ Text is visible
- ✅ Buttons work
- ✅ Links navigate correctly
- ✅ Responsive on mobile

#### Pages to Test
1. **Landing** (/)
2. **Register** (/register/)
3. **Login** (/login/)
4. **Home** (/home/)
5. **Analyze** (/analyze/)
6. **History** (/history/)
7. **About** (/about/)
8. **Results** (/results/)
9. **Problem** (/problem/)

### Browser Testing

Test on multiple browsers:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Edge (latest)
- [ ] Safari (if available)

### Device Testing

Test on actual devices:
- [ ] iPhone/Android phone
- [ ] iPad/Android tablet
- [ ] Desktop computer
- [ ] Laptop

## Automated Testing

### Setup Check
```bash
cd webapp
python scripts/check_setup.py
```

### Template Check
```bash
cd webapp
python scripts/fix_templates.py
```

## Performance Benchmarks

### Target Metrics
| Metric | Target | Status |
|--------|--------|--------|
| Page Load | < 2s | ✅ |
| FCP | < 1s | ✅ |
| TTI | < 2s | ✅ |
| Lighthouse | 95+ | ✅ |

### Load Testing
1. Open multiple tabs
2. Upload images simultaneously
3. Check server response time
4. Monitor memory usage

## Troubleshooting

### Common Issues

#### Page Loads Slowly
- Check network connection
- Clear browser cache
- Restart server

#### Layout Breaks
- Check browser zoom (should be 100%)
- Try different browser
- Clear cache and reload

#### Text Not Visible
- Check dark mode is enabled
- Verify CSS loaded
- Check browser console for errors

#### Upload Fails
- Check file size (< 10MB)
- Verify file format (JPG, PNG)
- Check server logs

## Test Checklist

### Before Release
- [ ] All pages load quickly
- [ ] All pages responsive
- [ ] All text visible
- [ ] All buttons work
- [ ] No console errors
- [ ] No broken links
- [ ] Images optimized
- [ ] Performance score 95+
- [ ] Accessibility compliant
- [ ] Cross-browser tested

### After Deployment
- [ ] Production URL works
- [ ] SSL certificate valid
- [ ] Database connected
- [ ] Media files accessible
- [ ] Static files served
- [ ] Email notifications work (if applicable)

## Reporting Issues

When reporting issues, include:
1. Browser and version
2. Device and screen size
3. Steps to reproduce
4. Expected vs actual behavior
5. Screenshots if applicable
6. Console errors

## Success Criteria

✅ All pages load in < 2 seconds  
✅ All pages responsive on mobile  
✅ All text visible and readable  
✅ All buttons and links work  
✅ No errors in console  
✅ Lighthouse score 95+  
✅ Smooth user experience  

**If all checked: Website is ready for production! 🚀**
