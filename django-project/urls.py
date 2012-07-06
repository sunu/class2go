from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'c2g.views.home'),
    # url(r'^class2go/', include('class2go.foo.urls')),

    # accounts app for user management
	url(r'^accounts/profile/', 'accounts.views.profile'),
	url(r'^accounts/', include('registration.backends.simple.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	
	# Developer utility to populate db with test data.
	url(r'^db_populate$', 'c2g.views.db_populate'),
	
	# The following line is temprarily commented out until we figure out how django cascades its URL matching operations.
	# After this is figured out, the rest of the matches below shall be moved to courses.url.
	#url(r'.*', include('courses.urls')),
	
	url(r'^courses/new/?', 'courses.admin_views.new'),
	
	url(r'^courses/all/?', 'courses.views.all'),
	url(r'^courses/current/?', 'courses.views.current'),
	url(r'^courses/mine/?', 'courses.views.mine'),
	
	url(r'^(?P<course_id>[a-z0-9_]+)/?$', 'courses.views.view'),
	url(r'^(?P<course_id>[a-z0-9_]+)/admin/?', 'courses.admin_views.admin'),
	url(r'^(?P<course_id>[a-z0-9_]+)/staff/?', 'courses.admin_views.staff'),
	
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/?$', 'courses.branches.views.view'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/admin/?', 'courses.branches.views.admin'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/members/?', 'courses.branches.views.members'),
	
	# Additional Pages
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/additional_pages/?$', 'courses.additional_pages.views.list'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/additional_pages/admin/?', 'courses.additional_pages.views.admin'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/additional_pages/(?P<additional_page_id>[a-z0-9_]+)/edit/?', 'courses.additional_pages.views.edit'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/additional_pages/(?P<additional_page_id>[a-z0-9_]+)/?$', 'courses.additional_pages.views.view'),

	# Announcements
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/announcements/?$', 'courses.announcements.views.list'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/announcements/admin/?', 'courses.announcements.views.admin'),
	
	# Assignments
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/assignments/?$', 'courses.assignments.views.list'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/assignments/admin/?', 'courses.assignments.views.admin'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/assignments/(?P<assignment_id>[a-z0-9_]+)/?$', 'courses.assignments.views.view'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/assignments/(?P<assignment_id>[a-z0-9_]+)/edit/?', 'courses.assignments.views.edit'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/assignments/(?P<assignment_id>[a-z0-9_]+)/grade/?', 'courses.assignments.views.grade'),
	
	# Files
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/files/?$', 'courses.files.views.list'),
	
	# Forums
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/forums/?$', 'courses.forums.views.view'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/forums/admin/?', 'courses.forums.views.admin'),
	
	# Lectures
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/lectures/?$', 'courses.lectures.views.list'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/lectures/admin/?', 'courses.lectures.views.admin'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/lectures/(?P<lecture_id>[a-z0-9_]+)/?$', 'courses.lectures.views.view'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/lectures/(?P<lecture_id>[a-z0-9_]+)/edit/?', 'courses.lectures.views.edit'),
	
	# Office Hours
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/officehours/?$', 'courses.officehours.views.list'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/officehours/admin/?', 'courses.officehours.views.admin'),
	
	# Sections
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/sections/?$', 'courses.sections.views.list'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/sections/admin/?', 'courses.sections.views.admin'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/sections/(?P<section_id>[a-z0-9_]+)/?$', 'courses.sections.views.view'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/sections/(?P<section_id>[a-z0-9_]+)/edit/?', 'courses.sections.views.edit'),
	
	# Videos
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/videos/?$', 'courses.videos.views.list'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/videos/admin/?', 'courses.videos.views.admin'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/videos/(?P<video_id>[a-z0-9_]+)/?$', 'courses.videos.views.view'),
	url(r'^(?P<course_id>[a-z0-9_]+)/(?P<branch_id>[a-z0-9_]+)/videos/(?P<video_id>[a-z0-9_]+)/edit/?', 'courses.videos.views.edit'),
)